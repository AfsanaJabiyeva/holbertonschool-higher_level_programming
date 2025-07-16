#!/usr/bin/python3

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
auth = HTTPBasicAuth()
jwt = JWTManager(app)
users = {
    "afsana": {
        "password": generate_password_hash("hello"),
        "role": "user"
    },

    "admin": {
        "password": generate_password_hash("adminpswd"),
        "role": "admin"
    }
}
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username)["password"], password):
        return username
    else:
        return None
@app.route('/basic-protected')
@auth.login_required
def basic():
    return jsonify({"Basic Auth": "Access Granted"})

@app.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    username =data.get("username", None)
    password = data.get("password", None)

    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"message": "Bad username or password"}), 401

    access_token = create_access_token(identity={"username": username, "role":user["role"]})
    return jsonify(access_token=access_token)


@app.route('/jwt-protected', methods=["GET"])
@jwt_required()
def protected():
    return jsonify({"message": "JWT Auth: Access Granted"}), 200

@app.route('/onlyadmin')
@jwt_required()
def only_admin():
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        return jsonify({"message": "Access Granted!"})
    else:
        return jsonify({"message": "No Access!"}), 403

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401
if __name__=="__main__":
    app.run()
