"""Module for auth views (controllers) testing"""

import json
import time
from base64 import b64encode

from flask import Response

from auth.models import User
from auth.services import encode_auth_token
from auth.tests import BaseCase
from utils import db

EXPIRED_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.' \
                'eyJleHAiOjE2MjE5NjQ2NDgsImlhdCI6MTYyM' \
                'Tk2NDY0Nywic3ViIjoidXNlcl9pZCJ9.ykZq7d3' \
                'RUW2gCXsSmTKJw0pm8AmiLjzDN4VS6HXCYNY'


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
    return self.client.post(
        "/auth/login",
        data=json.dumps({"username": username,
                         "password": password}),
        headers={"Content-Type": "application/json",
                 "Authorization": f"Basic {credentials}"}
    )


class TestRegistrationView(BaseCase):
    """Class for testing registration view"""

    def test_registration(self) -> None:
        """Test for user registration"""
        response = self.client.post(
            "/auth/registration",
            data=json.dumps({"username": "username",
                             "email": "email@gmail.com"}),
            headers={"Content-Type": "application/json"}
        )
        self.assertEqual(response.status_code, 400)

    def test_registration_wrong_data(self) -> None:
        """Test for user registration if wrong data"""
        response = register_user(self, "user", "example@gmail.com", "pass123")
        self.assertEqual(response.json["message"], "Successfully registered")
        self.assertEqual(response.status_code, 201)

    def test_registered_with_already_registered_user(self) -> None:
        """Test registration with already registered username or email"""
        user = User(username="user",
                    email="example@gmail.com",
                    password="pass123")
        db.session.add(user)
        db.session.commit()
        response = register_user(self, "user", "other@gmail.com", "pass321")
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json["message"], "Such user exists")


class TestLoginView(BaseCase):
    """Class for testing login view"""

    def test_registered_user_login_by_email(self):
        """ Test for login of registered user by email"""
        response = register_user(self, "user", "example@gmail.com", "pass123")
        self.assertEqual(response.json['message'], 'Successfully registered')
        self.assertEqual(response.status_code, 201)

        response = login_user(self, 'example@gmail.com', 'pass123')
        self.assertEqual(response.json['message'], 'Successfully logged in')
        self.assertTrue(response.json['token'])
        self.assertEqual(response.status_code, 200)

    def test_registered_user_login_by_username(self):
        """ Test for login of registered user by username """
        response = register_user(self, "user", "example@gmail.com", "pass123")
        self.assertEqual(response.json['message'], 'Successfully registered')
        self.assertEqual(response.status_code, 201)

        response = login_user(self, 'user', 'pass123')
        self.assertEqual(response.json['message'], 'Successfully logged in')
        self.assertTrue(response.json['token'])
        self.assertEqual(response.status_code, 200)

    def test_non_registered_user_login(self):
        """ Test for login of non-registered user """
        response = login_user(self, 'joe@gmail.com', '123456')
        self.assertEqual(response.json['message'],
                         "User doesn't exist or wrong password")
        self.assertEqual(response.status_code, 404)

    def test_login_without_auth(self):
        """ Test for login of user without 'Authorization' header"""
        response = register_user(self, "user", "example@gmail.com", "pass123")
        self.assertEqual(response.json['message'], 'Successfully registered')
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            "/auth/login",
            data=json.dumps({"username": 'user',
                             "password": 'pass123'}),
            headers={"Content-Type": "application/json"})
        self.assertEqual(response.headers['WWW-Authenticate'],
                         "Basic realm='Authentication required'")
        self.assertEqual(response.json['message'], "Authentication required")
        self.assertEqual(response.status_code, 401)


class TestLogoutView(BaseCase):
    """Class for testing logout view"""

    def test_logout_logged_in_user(self):
        """Test user logout if user logged-in"""
        response = register_user(self, "user", "example@gmail.com", "pass123")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Successfully registered')

        response = login_user(self, 'example@gmail.com', 'pass123')
        self.assertEqual(response.json['message'], 'Successfully logged in')
        self.assertEqual(response.status_code, 200)

        token = response.json["token"]
        response = self.client.get("/auth/logout",
                                   headers={"Authorization": f"Bearer {token}"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Successfully logged out")

    def test_logout_without_header(self):
        """Test user logout if request hasn't necessary header"""
        response = self.client.get("/auth/logout")
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.headers["WWW-Authenticate"],
                         "Bearer realm='Token required'")
        self.assertEqual(response.json['message'], "Authentication required")

    def test_logout_without_token(self):
        """Test user logout if request hasn't token in header"""
        response = self.client.get("/auth/logout",
                                   headers={"Authorization": "Bearer "})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.headers["WWW-Authenticate"],
                         "Bearer realm='Token required'")
        self.assertEqual(response.json['message'], "Authentication required")

    def test_logout_invalid_token(self):
        """Test user logout if request has invalid token"""
        response = self.client.get("/auth/logout",
                                   headers={"Authorization": "Bearer abc123"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["message"], "Invalid token")

    def test_logout_expired_token(self):
        """Test user logout if request has expired token"""
        expired_token = encode_auth_token("user_id", {"seconds": 0})
        time.sleep(1)
        response = self.client.get(
            "/auth/logout",
            headers={"Authorization": f"Bearer {expired_token}"})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json["message"], "Signature expired")
