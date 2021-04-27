import unittest
from auth.models import User


class TestUserModel(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User(password="pass")
        self.user2 = User(password="pass")

    def test_password_setter(self):
        self.assertIsNotNone(self.user.password_hash)

    def test_no_password_getter(self):
        with self.assertRaises(AttributeError):
            self.user.password

    def test_password_verification(self):
        self.assertTrue(self.user.verify_password("pass"))
        self.assertFalse(self.user.verify_password("fake_pass"))

    def test_password_salts_are_random(self):
        self.assertTrue(self.user.password_hash != self.user2.password_hash)