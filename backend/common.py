"""Module for common function and decorators"""

from functools import wraps

import jwt
from flask import request

from auth.models import User
from auth.services import decode_auth_token
from utils import db


def token_required(function):
    """Function to check user token"""
    @wraps(function)
    def wrapper(*args, **kwargs):
        token = request.headers.get("X-API-KEY", '')
        print(token)
        if not token:
            return {"message": "Token should be provided"}, 401
        try:
            uuid = decode_auth_token(token)["sub"]
        except (KeyError, jwt.ExpiredSignatureError):
            return {"message": "Signature expired. Please log in again"}, 401
        except jwt.InvalidTokenError:
            return {"message": 'Invalid token. Please log in again.'}, 401
        user = db.session.query(User).filter_by(uuid=uuid).first()
        if not user:
            return {"message": "User doesn't exist"}, 401
        return function(*args, **kwargs)
    return wrapper
