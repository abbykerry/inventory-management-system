from flask import Flask


def create_app():
    #This function creates and configures the Flask application.

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "super-secret-key"  # will improve this later
    #importing and registering blueprints.
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    return app