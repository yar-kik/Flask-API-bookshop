"""Module for auth controllers (views)"""
from datetime import timedelta

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError

from auth.models import User
from auth.schemas import UserSchema
from common import token_required, get_token, encode_auth_token, send_email
from config import TOKEN_EXPIRATION
from utils import db, cache


class RegisterApi(Resource):
    """Class for user registration"""
    user_schema = UserSchema()

    def post(self):
        """Function for creating new user"""
        try:
            user = self.user_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {"message": str(e)}, 400
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return {"message": "User with this username "
                               "or email already exists"}, 409
        send_email.apply_async(args=["Successful registration!",
                                     [user.email],
                                     "You have been successfully registered"])
        return {"user": self.user_schema.dump(user),
                "message": "Successfully registered"}, 201


class LoginApi(Resource):
    """Class for user login"""

    # pylint: disable=no-self-use
    def post(self):
        """Function for user login"""
        auth = request.authorization
        if not auth:
            return {"message": "Authentication required"}, 401, \
                   {"WWW-Authenticate": "Basic realm='Authentication required'"}
        username = auth.get("username", '')
        user = db.session.query(User).filter(
            or_(User.username == username, User.email == username)).first()
        if not user or not user.verify_password(auth.get("password", '')):
            return {"message": "User doesn't exist or wrong password"}, 404
        token = encode_auth_token(user.uuid, TOKEN_EXPIRATION, user.is_admin)
        return {"message": "Successfully logged in",
                "token": token}, 200


class LogoutApi(Resource):
    """Class for user logout"""

    # pylint: disable=no-self-use
    @token_required
    def get(self):
        """Function for user logout"""
        token = get_token()
        cache.add(f"blacklisted_token:{token}", token,
                  timeout=int(timedelta(**TOKEN_EXPIRATION).total_seconds()))
        return {"message": "Successfully logged out"}, 200
