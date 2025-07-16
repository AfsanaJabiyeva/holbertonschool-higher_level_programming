#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["SECRET_KEY"] = "some-other-secret"
auth = HTTPBasicAuth()
jwt_app = JWTManager(app)


users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    checked_user = users.get(username)

    if checked_user and check_password_hash(checked_user["password"], password):
        return checked_user

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify({"Basic Auth": "Access Granted"})

@app.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", None)
    password = data.get("password", None)

    current_user = users.get(username)

    if current_user and check_password_hash(current_user["password"], password):

        access_token = create_access_token(identity=current_user)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"message": "Bad username or password"}), 401

@app.route('/jwt-protected', methods=["GET"])
@jwt_required()
def jwt_protected():
    return jsonify({"message": "JWT Auth: Access Granted"}), 200

@app.route('/admin-only', methods=["GET"])
@jwt_required()
def admin_only():
    user = get_jwt_identity()
    if user["role"] == "admin":
        return jsonify({"message": "Admin Access: Granted"})
    else:
        return jsonify({"error": "Admin access required"}), 403


@jwt_app.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt_app.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt_app.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt_app.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt_app.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run()
