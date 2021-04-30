from functools import wraps

import jwt
from flask import request, current_app

from auth.models import User
from utils import db


def token_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        token = request.headers.get("X-API-KEY", '')
        print(token)
        if not token:
            return "", 401, \
                   {"WWW-Authenticate": "Basic realm='Authentication required'"}
        try:
            print(current_app.config["SECRET_KEY"])
            uuid = jwt.decode(token, current_app.config["SECRET_KEY"],
                              algorithms=["HS256"])["user_id"]
        except (KeyError, jwt.ExpiredSignatureError):
            return "", 401, \
                   {"WWW-Authenticate": "Basic realm='Authentication required'"}
        user = db.session.query(User).filter_by(uuid=uuid).first()
        if not user:
            return "", 401, \
                   {"WWW-Authenticate": "Basic realm='Authentication required'"}
        return function(*args, **kwargs)

    return wrapper
