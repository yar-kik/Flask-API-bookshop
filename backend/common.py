"""Module for common functions and decorators"""

from functools import wraps
from typing import Callable

import jwt
from flask import request

from auth.models import User
from auth.services import decode_auth_token
from utils import db, cache


def token_required(function: Callable):
    """Function to check user token"""
    @wraps(function)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header and not auth_header.split()[1:]:
            return {"message": "Authentication required"}, 401, \
                   {"WWW-Authenticate": "Bearer realm='Token required'"}
        token = auth_header.split()[1]
        if cache.get(f"blacklisted_token:{token}"):
            return {"message": "Token is already blacklisted"}, 403
        try:
            uuid = decode_auth_token(token)["sub"]
        except (KeyError, jwt.ExpiredSignatureError):
            return {"message": "Signature expired. Please log in again"}, 401
        except jwt.InvalidTokenError:
            return {"message": 'Invalid token. Please log in again.'}, 400
        user = db.session.query(User).filter_by(uuid=uuid).first()
        if not user:
            return {"message": "User doesn't exist"}, 404
        return function(*args, **kwargs)
    return wrapper
