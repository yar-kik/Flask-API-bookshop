"""Module for book database services"""

import datetime
from typing import Dict

import jwt
from flask import current_app


def encode_auth_token(user_id: str, expiration: Dict[str, int] = None) -> str:
    """Generates the Auth Token"""
    if expiration is None:
        expiration = {"minutes": 15}
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(**expiration),
        'iat': datetime.datetime.utcnow(),
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
                         current_app.config.get('SECRET_KEY'),
                         algorithms="HS256")
    return payload
