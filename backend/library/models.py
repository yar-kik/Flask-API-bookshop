"""Module for database entity"""
from werkzeug.security import generate_password_hash, check_password_hash

from utils import db


class Book(db.Model):
    """Class for book entity in database"""
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False, index=True)
    publisher = db.Column(db.String(64))
    author = db.Column(db.String(64), nullable=False)
    published = db.Column(db.Date)
    description = db.Column(db.Text)
    pages = db.Column(db.SmallInteger)
    category = db.Column(db.String(64))

    def __repr__(self):
        return f'Book ({self.title}), {self.author}'


class User(db.Model):
    """Class for user entity in database"""
    __tablname__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(128), nullable=False)

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
