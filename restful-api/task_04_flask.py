#!/usr/bin/python3
from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}
@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def usernameList():
    return jsonify(list(users.keys()))

@app.route('/status')
def statusEndpoint():
    return 'OK'

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods = ['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    if not data or 'username' not in data:
        return jsonify({"error":"Username is required"}), 400

    else:
        users[username] = {'username': username, 'name': data.get('name'), 'age': data.get('age'), 'city': data.get('city')}

    return jsonify({"message": "User added", "user":users[username]  }), 201

if __name__=="__main__":
    app.run()
