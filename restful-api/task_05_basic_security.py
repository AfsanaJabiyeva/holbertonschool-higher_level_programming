#!/usr/bin/python3
#!/usr/bin/python3

from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, get_jwt_identity, create_access_token, jwt_required

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'N?3lo!AQ@./'
app.config['SECRET_KEY'] = 'ah8(8:ksa,'
auth = HTTPBasicAuth()
jwt_app = JWTManager(app)

users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"),
              "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"),
               "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    checked_user = users.get(username)

    if username in users and check_password_hash(checked_user['password'], password):
        return users[username]


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login_jwt():
    username = request.json.get('username')
    password = request.json.get('password')
    current_user = users.get(username)
    if username in users and check_password_hash(current_user['password'], password):
        new_token = create_access_token(identity=current_user)
        return jsonify(access_token=new_token)
    return jsonify({"msg": "Bad username or password"}), 401


@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def check_token():
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def only_admins():
    user = get_jwt_identity()
    if user['role'] == 'admin':
        return "Admin Access: Granted"
    return jsonify({"error": "Admin access required"}), 403



@jwt_app.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt_app.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt_app.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt_app.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt_app.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
