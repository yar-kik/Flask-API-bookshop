"""Module for library database models"""

from uuid import uuid4
from utils import db
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """Class for user entity in database"""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    username = db.Column(db.String(32), nullable=False, unique=True,
                         index=True)
    _password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    uuid = db.Column(db.String(36))
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uuid = str(uuid4())
        self.password = kwargs['password']

    def __str__(self):
        return f"User {self.username}"

    @hybrid_method
    def verify_password(self, password: str) -> bool:
        """
        Return true if password_hash and password are equals
        """
        return check_password_hash(self._password, password)

    @hybrid_property
    def password(self) -> str:
        """Password getter"""
        return self._password

    @password.setter
    def password(self, new_password: str):
        """Password setter that automatically generate hash"""
        self._password = generate_password_hash(new_password)

    def save(self):
        """Save entity to database"""
        db.session.add(self)
        db.session.commit()
