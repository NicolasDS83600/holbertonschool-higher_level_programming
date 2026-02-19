#!/usr/bin/python3
"""A simple Flask API to manage user data with basic CRUD endpoints."""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.get("/")
def home():
    """Home route returning a welcome message."""
    return "Welcome to the Flask API!"


@app.get("/data")
def data():
    """Return a JSON list of all user data."""
    return jsonify(list(users.key()))


@app.get()
def get_username():
    """Return a JSON list of all usernames."""
    username = list(users.keys())
    return jsonify(username)


@app.get("/status")
def status():
    """Return API status message."""
    return "Ok"


@app.get("/users/<username>")
def user_check(username):
    """Return JSON data for a specific user, 404 if not found."""
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.post("/add_user")
def add_user():
    """Add a new user from JSON payload; returns errors if invalid."""
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    user_data = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
        }
    users[username] = user_data

    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run()
