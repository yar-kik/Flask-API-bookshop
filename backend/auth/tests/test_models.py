"""Module for test user model"""

import unittest
from auth.models import User


class TestUserModel(unittest.TestCase):
    """Class for user model testing"""

    def setUp(self) -> None:
        """Setting up test data and configs"""
        self.user = User(password="pass", username="user_name")
        self.user2 = User(password="pass")

    def test_model_str(self):
        """Test model representation"""
        self.assertEqual(str(self.user), "User user_name")

    def test_password_verification(self):
        """Test password verification"""
        self.assertTrue(self.user.verify_password("pass"))
        self.assertFalse(self.user.verify_password("fake_pass"))

    def test_password_salts_are_random(self):
        """Test passwords of different users are different"""
        self.assertTrue(self.user.password != self.user2.password)
