from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors
import firebase_admin
from firebase_admin import credentials, auth
from data_repository import User, UserRepository, UserRole

cred = credentials.Certificate("C:/Dev/nzhf-database-firebase-adminsdk-yb01r-facef03988.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

class Server:
    def __init__(self, user_repo) -> None:
        self.user_repo = user_repo
    
    def with_user(method):
        # creates a decorator for methods, trying to extract user
        # from the request then calling the method with it
        # or sending back error message
        def wrapper(self, *args, **kwargs):
            try:
                signed_in_user = self._get_user()
                return method(self, signed_in_user, *args, **kwargs)
            except auth.ExpiredIdTokenError:
                return jsonify({'error': 'Token has expired'}), 401
            except auth.InvalidIdTokenError:
                return jsonify({'error': 'Invalid token'}), 401
        return wrapper

    @with_user
    def login(self, signed_in_user):
        return jsonify({'full_name': signed_in_user.full_name, 'role': signed_in_user.role.name})

    @with_user
    def users(self, signed_in_user):
        return jsonify(self._get_users(signed_in_user))
    
    @with_user
    def create_user(self, signed_in_user):
        return jsonify({'error': 'not implemented'}), 401
        
    def _get_users(self, signed_in_user):
        if signed_in_user.role == UserRole.NZHF_ADMIN:
            # only admins have access to all users
            return [{'full_name': u.full_name, 'role': u.role.name} for u in self.user_repo.get_all()]
        return []
   
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

user_repo = UserRepository()
server = Server(user_repo)

@app.route('/login', methods=['POST'])
def login():
    return server.login()

@app.route('/users', methods=['GET'])
def users():
    return server.users()

if __name__ == '__main__':
    app.run(debug=True)