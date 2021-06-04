"""Init module for testing"""
import json
import unittest
from base64 import b64encode

from flask import Response

from auth.models import User
from library.models import Book
from utils import create_app, db


def register_user(self, username: str, email: str, password: str) -> Response:
    """Function to register new user"""
    return self.client.post(
        "/auth/registration",
        data=json.dumps({"username": username,
                         "email": email,
                         "password": password}),
        headers={"Content-Type": "application/json"}
    )


def login_user(self, username: str, password: str) -> Response:
    """Function to login user"""
    user_data = f"{username}:{password}".encode("utf-8")
    credentials = b64encode(user_data).decode('utf-8')
    return self.client.get(
        "/auth/login",
        headers={"Content-Type": "application/json",
                 "Authorization": f"Basic {credentials}"}
    )


def create_user() -> User:
    """Create new simple user"""
    user = User(
        username="user",
        email='example@gmail.com',
        password='pass123'
    )
    db.session.add(user)
    db.session.commit()
    return user


def create_admin() -> User:
    """Create new admin user"""
    admin = User(username="user",
                 email="example@gmail.com",
                 password="pass123",
                 is_admin=True)
    db.session.add(admin)
    db.session.commit()
    return admin


def create_book() -> Book:
    """Create new book"""
    book = Book(title="Book title",
                author="Book author",
                price=200)
    db.session.add(book)
    db.session.commit()
    return book


class BaseCase(unittest.TestCase):
    """Base test configurations"""

    def setUp(self) -> None:
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app.app_context().push()
        db.create_all()
        self.book_data = json.dumps({"title": "Single Book",
                                     "author": "Book author",
                                     "price": 200})
        self.headers = {"Content-Type": "application/json"}

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()


class AdminCase(BaseCase):
    """Admin test configurations"""

    def setUp(self) -> None:
        super().setUp()
        create_admin()
        response = login_user(self, 'example@gmail.com', 'pass123')
        token = response.json["token"]
        self.headers = {"Authorization": f"Bearer {token}",
                        "Content-Type": "application/json"}
