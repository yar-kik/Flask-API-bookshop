"""Module for testing common functions and decorators"""

import time

from auth.tests.test_views import login_user
from common import get_token, encode_auth_token
from tests import BaseCase, create_book, create_user, create_admin


class TestCommon(BaseCase):
    """Test common functions and decorators"""

    def test_token_required_without_token(self):
        """Test token_required decorator if request hasn't token in header"""
        response = self.client.get("/auth/logout",
                                   headers={"Authorization": "Bearer "})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.headers["WWW-Authenticate"],
                         "Bearer realm='Token required'")
        self.assertEqual(response.json['message'], "Authentication required")

    def test_token_required_invalid_token(self):
        """Test user logout if request has invalid token"""
        response = self.client.get("/auth/logout",
                                   headers={"Authorization": "Bearer abc123"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["message"],
                         "Invalid token. Please log in again.")

    def test_token_required_expired_token(self):
        """Test token_required decorator if request has expired token"""
        expired_token = encode_auth_token("user_id", {"seconds": 0})
        time.sleep(1)
        response = self.client.get(
            "/auth/logout",
            headers={"Authorization": f"Bearer {expired_token}"})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json["message"],
                         "Signature expired. Please log in again")

    def test_get_token_if_no_header(self):
        """Test get_token function if request hasn't necessary header"""
        with self.app.test_request_context("/auth/logout"):
            token = get_token()
            self.assertIsNone(token)

    def test_admin_required_if_admin(self):
        """Test admin_required decorator if user is admin"""
        create_book()
        create_admin()
        response = login_user(self, 'example@gmail.com', 'pass123')
        token = response.json["token"]
        response = self.client.delete("/books/1",
                                      headers={
                                          "Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 204)
        self.assertFalse(response.data)

    def test_admin_required_if_not_admin(self):
        """Test admin_required decorator if user is not admin"""
        create_book()
        create_user()
        response = login_user(self, 'example@gmail.com', 'pass123')
        token = response.json["token"]
        response = self.client.delete("/books/1",
                                      headers={
                                          "Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json["message"], "Admin rights required")

    def test_encode_auth_token(self):
        """Test auth token encode"""
        user = create_user()
        auth_token = encode_auth_token(user.uuid)
        self.assertTrue(isinstance(auth_token, str))
