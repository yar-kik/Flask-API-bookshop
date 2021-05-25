"""Module for library database models"""

from uuid import uuid4
from utils import db
from sqlalchemy.ext.hybrid import hybrid_method
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """Class for user entity in database"""
    __tablename__ = "users"

    # TODO: first/last name, date register, phone number?
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    username = db.Column(db.String(64), nullable=False, unique=True,
                         index=True)  # TODO: change to length 32
    password = db.Column(db.String(128), nullable=False)
    uuid = db.Column(db.String(36))  # TODO: add index=True
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uuid = str(uuid4())
        self.password = generate_password_hash(kwargs['password'])

    def __str__(self):
        return f"User {self.username}"

    @hybrid_method
    def verify_password(self, password: str) -> bool:
        """
        Return true if password_hash and password are equals
        """
        return check_password_hash(self.password, password)
