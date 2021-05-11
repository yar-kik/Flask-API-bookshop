"""Init module for testing"""

import unittest

from utils import create_app, db


class BaseCase(unittest.TestCase):
    """Base test configurations"""

    def setUp(self) -> None:
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app.app_context().push()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
