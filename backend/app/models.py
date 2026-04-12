from app import db
from werkzeug.security import generate_password_hash, check_password_hash


# Role model
class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    # relationship: one role - many users
    users = db.relationship("User", backref="role", lazy=True)


# User model
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    # foreign key (link to Role)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)

    # password hashing methods
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)