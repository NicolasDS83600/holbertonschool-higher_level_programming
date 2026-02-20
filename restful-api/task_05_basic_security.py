#!/usr/bin/python3
"""Flask app with Basic Auth and JWT role-based authentication."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
    )

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-in-production"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"), "role": "user"
        },
    "admin1": {
        "username": "admin1", "password": generate_password_hash("password"),
        "role": "admin"
        }
}


@auth.verify_password
def verify_password(username, password):
    """Verify username and password for Basic Auth."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.get("/basic-protected")
@auth.login_required
def basic_protected():
    """Basic Auth protected endpoint."""
    return jsonify("Basic Auth: Access Granted")


@app.post("/login")
def login():
    """Authenticate user and return JWT access token."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    token = create_access_token(
        identity=username, additional_claims={"role": user["role"]}
        )
    return jsonify({"access_token": token})


@app.get("/jwt-protected")
@jwt_required()
def jwt_protected():
    """JWT-protected endpoint accessible to any authenticated user."""
    return jsonify("JWT Auth: Access Granted")


@app.get("/admin-only")
@jwt_required()
def admin_only():
    """JWT-protected endpoint accessible only to admin users."""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify("Admin Access: Granted")


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid JWT."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_data):
    """Handle expired JWT token."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_data):
    """Handle revoked JWT token."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_data):
    """Handle cases where a fresh token is required."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
