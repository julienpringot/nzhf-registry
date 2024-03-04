from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors
import firebase_admin
from firebase_admin import credentials, auth
from mock_data import MockUserRepo
from user_repository import User, UserRole

cred = credentials.Certificate("C:/Dev/nzhf-database-firebase-adminsdk-yb01r-facef03988.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

class Server:
    def __init__(self, user_repo) -> None:
        self.user_repo = user_repo
    
    def with_user(method):
        def wrapper(self, *args, **kwargs):
            try:
                user = self._get_user()
                return method(self, user, *args, **kwargs)
            except auth.ExpiredIdTokenError:
                return jsonify({'error': 'Token has expired'}), 401
            except auth.InvalidIdTokenError:
                return jsonify({'error': 'Invalid token'}), 401
        return wrapper

    @with_user
    def login(self, user):
        return jsonify({'username': user.full_name, 'usertype': user.role.name})

    @with_user
    def users(self, user):
        # retrieve the user sending the request
        # then sends back all other users for NZHF Admin
        # or empty list for Club Admin
        if user.role is UserRole.NZHF_ADMIN:
            return jsonify({'username': user.full_name, 'usertype': user.role.name} for user in self.user_repo)
        else:
            return jsonify([])
   
    def _extract_bearer_token(self):
        # Get the Authorization header from the request
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return None  # No Authorization header found

        # Check if the header starts with 'Bearer '
        if not auth_header.startswith('Bearer '):
            return None  # Invalid format

        # Extract the token excluding 'Bearer '
        return auth_header[len('Bearer '):]

    # calls extract_bearer_token(), retrieves the email then get user information
    def _get_user(self) -> User:
        id_token = self._extract_bearer_token()
        # Verify the ID token
        decoded_token = auth.verify_id_token(id_token)

        # Extract user information
        email = decoded_token.get('email')
        return self.user_repo.get(email)

server = Server(MockUserRepo)


@app.route('/login', methods=['POST'])
def login():
    return server.login()

@app.route('/users', methods=['GET'])
def users():
    return server.users()

if __name__ == '__main__':
    app.run(debug=True)