from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = "super-secret-key"
    jwt = JWTManager(app)

    db.init_app(app)

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    # import and register blueprints
    #from app.routes import product_bp
    #app.register_blueprint(product_bp)

    with app.app_context():
        db.create_all()

    return app