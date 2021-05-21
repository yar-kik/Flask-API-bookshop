"""Module for book database services"""

import datetime
import jwt
from flask import current_app


def encode_auth_token(user_id: str) -> str:
    """Generates the Auth Token"""
    payload = {
        'exp': datetime.datetime.now() + datetime.timedelta(minutes=15),
        'iat': datetime.datetime.now(),
        'sub': user_id
    }
    return jwt.encode(
        payload,
        current_app.config.get('SECRET_KEY'),
        algorithm='HS256'
    )


def decode_auth_token(auth_token: str) -> dict:
    """Decodes the auth token"""
    payload = jwt.decode(auth_token,
                         current_app.config.get('SECRET_KEY'))
    return payload
