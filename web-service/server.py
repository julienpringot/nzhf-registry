from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors
import firebase_admin
from firebase_admin import credentials, auth
from user_repository import User, UserRepository
cred = credentials.Certificate("./nzhf-database-firebase-adminsdk-diwyt-3616a4d956.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

user_repository = UserRepository()

def extract_bearer_token():
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
def get_user() -> User:
    id_token = extract_bearer_token()
    # Verify the ID token
    decoded_token = auth.verify_id_token(id_token)

    # Extract user information
    email = decoded_token.get('email')
    return user_repository.get(email)
    
@app.route('/login', methods=['POST'])
def login():
    try:
        user = get_user()

        return jsonify({'username': user.full_name, 'usertype': user.role.name})
    except auth.ExpiredIdTokenError:
        return jsonify({'error': 'Token has expired'}), 401
    except auth.InvalidIdTokenError:
        return jsonify({'error': 'Invalid token'}), 401

@app.route('/users', methods=['GET'])
def users():
    # retrieve the user sending the request
    # then sends back all other users for NZHF Admin
    # or empty list for Club Admin
    pass

if __name__ == '__main__':
    app.run(debug=True)