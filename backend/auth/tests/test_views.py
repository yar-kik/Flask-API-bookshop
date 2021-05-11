"""Module for auth views (controllers) testing"""

import json
from base64 import b64encode

from flask import Response

from auth.models import User
from auth.tests import BaseCase
from utils import db


def register_user(self, username: str, email: str, password: str) -> Response:
    """Function to register new user"""
    return self.client.post(
        "/auth/register",
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
        data=json.dumps({"username": username,
                         "password": password}),
        headers={"Content-Type": "application/json",
                 "Authorization": f"Basic {credentials}"}
    )


class TestAuthViews(BaseCase):
    """Class for auth views testing"""

    def test_registration(self) -> None:
        """Test for user registration"""
        response = self.client.post(
            "/auth/register",
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

        response = self.client.get(
            "/auth/login",
            data=json.dumps({"username": 'user',
                             "password": 'pass123'}),
            headers={"Content-Type": "application/json"})
        self.assertEqual(response.json['message'], "Authentication required")
        self.assertEqual(response.status_code, 401)
