"""Init module for testing"""
import json
import unittest

from auth.models import User
from auth.tests.test_views import login_user
from utils import create_app, db


def create_admin():
    """Create new admin user"""
    user = User(username="user",
                email="example@gmail.com",
                password="pass123",
                is_admin=True)
    db.session.add(user)
    db.session.commit()


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
        create_admin()
        response = login_user(self, 'example@gmail.com', 'pass123')
        token = response.json["token"]
        self.headers = {"Authorization": f"Bearer {token}",
                        "Content-Type": "application/json"}

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
