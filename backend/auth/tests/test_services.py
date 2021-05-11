"""Module for testing auth services"""

from auth.models import User
from auth.services import encode_auth_token
from auth.tests import BaseCase
from utils import db


class TestUserModel(BaseCase):
    """Class for testing user db services"""

    def test_encode_auth_token(self):
        """Test auth token encode"""
        user = User(
            username="username",
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        auth_token = encode_auth_token(user.uuid)
        self.assertTrue(isinstance(auth_token, str))
