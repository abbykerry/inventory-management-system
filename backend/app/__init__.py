from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #database instance

def create_app():
    #This function creates and configures the Flask application.

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "super-secret-key"  # will improve this later
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app) #connecting the database with the Flask app

    from app import models
    #importing and registering blueprints.
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    return app