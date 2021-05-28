"""Module for common functions and decorators"""

import datetime
from functools import wraps
from typing import Callable, Optional, Dict

from flask import request, current_app
import jwt

from utils import cache


def encode_auth_token(user_id: str,
                      expiration: Dict[str, int] = None,
                      admin: bool = False) -> str:
    """Generates the Auth Token"""
    if expiration is None:
        expiration = {"minutes": 15}
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(**expiration),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id,
        'admin': admin
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


def get_token() -> Optional[str]:
    """Get token from header"""

    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.split()[1:]:
        return auth_header.split()[1]
    return None


def token_required(function: Callable):
    """Decorator to check user token"""

    @wraps(function)
    def wrapper(*args, **kwargs):
        token = get_token()
        if token is None:
            return {"message": "Authentication required"}, 401, \
                   {"WWW-Authenticate": "Bearer realm='Token required'"}
        if cache.get(f"blacklisted_token:{token}"):
            return {"message": "Token is already blacklisted"}, 403
        try:
            decode_auth_token(token)
        except jwt.ExpiredSignatureError:
            return {"message": "Signature expired. Please log in again"}, 401
        except jwt.InvalidTokenError:
            return {"message": 'Invalid token. Please log in again.'}, 400
        return function(*args, **kwargs)

    return wrapper


def admin_required(function: Callable):
    """Decorator to check if user is admin"""

    @wraps(function)
    def wrapper(*args, **kwargs):
        token = get_token()
        payload = decode_auth_token(token)
        if not payload["admin"]:
            return {"message": "Admin rights required"}, 403
        return function(*args, **kwargs)

    return wrapper
