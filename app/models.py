# This module defines the DB Schema
# Once flask-migrations is installed, can run 'flask db init' in terminal
# to set up migrations

from app import db


# Model Definitions
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User {self.username}"

