# This module defines the DB Schema
# Once flask-migrations is installed, can run 'flask db init' in terminal
# to set up migrations
# 'flask db migrate' will generate automatic migration scripts (and initialize db if not existing)
# You need to run 'flask db upgrade' to apply the migration
# You can run 'flask db downgrade' to revert to the previous migration

from app import db


# Model Definitions
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User {self.username}"

