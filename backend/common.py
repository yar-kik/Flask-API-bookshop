"""Module for common functions and decorators"""

from functools import wraps
from typing import Callable, Optional

import jwt
from flask import request

from auth.services import decode_auth_token
from utils import cache


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
            decode_auth_token(token)["sub"]
        except (KeyError, jwt.ExpiredSignatureError):
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
