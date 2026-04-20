from flask import Blueprint, jsonify, request
from app import db
from app.models import User, Role

# Create a blueprint for auth routes
auth_bp = Blueprint("auth", __name__)
#blueprint is a way to organize a group of related routes and functions in Flask. It allows us to modularize our application and keep related code together.

@auth_bp.route("/auth/test", methods=["GET"])
def test_auth():
    """
    This is a simple test route to confirm that auth routes are working.
    """
    return jsonify({"message": "Auth route is working"}), 200

@auth_bp.route("/auth/register", methods=["POST"])
def register():
    """
    Register a new user.
    Expected input: { email, password }
    """

    # 1. Get data from frontend request
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    # 2. Basic validation (making sure fields are not empty)
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    # 3. Check if user already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "User already exists"}), 409


    # 4. Get or create default role
    role = Role.query.filter_by(name="user").first()
    if not role:
        role = Role(name="user")
        db.session.add(role)
        db.session.commit()

    # 5. Create new user
    new_user = User(email=email, role_id=role.id)
    new_user.set_password(password)

    # 6. Save to database
    db.session.add(new_user)
    db.session.commit()

    # 7. Return success response
    return jsonify({
        "message": "User created successfully",
        "user": {
            "id": new_user.id,
            "email": new_user.email,
            "role": role.name
        }
    }), 201