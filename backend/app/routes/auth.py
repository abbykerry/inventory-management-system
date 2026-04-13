from flask import Blueprint, jsonify

# Create a blueprint for auth routes
auth_bp = Blueprint("auth", __name__)
#blueprint is a way to organize a group of related routes and functions in Flask. It allows us to modularize our application and keep related code together.

@auth_bp.route("/auth/test", methods=["GET"])
def test_auth():
    """
    This is a simple test route to confirm that auth routes are working.
    """
    return jsonify({"message": "Auth route is working"}), 200