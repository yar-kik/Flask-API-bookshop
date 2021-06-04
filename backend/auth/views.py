"""Module for auth controllers (views)"""
from datetime import timedelta

import jwt
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError

from auth.models import User
from auth.schemas import UserSchema
from common import token_required, get_token, encode_auth_token, send_email, \
    decode_auth_token
from config import TOKEN_EXPIRATION, LINK_EXPIRATION
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
            user.save()
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
    def get(self):
        """Function for user login"""
        auth = request.authorization
        if not auth:
            return {"message": "Authentication required"}, 401, \
                   {"WWW-Authenticate": "Basic realm='Authentication required'"}
        username = auth.get("username", '')
        password = auth.get("password", '')
        user = db.session.query(User).filter(
            or_(User.username == username, User.email == username)).first()
        if not user or not user.verify_password(password):
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


class SendResetLinkApi(Resource):
    """Class to reset password via email"""

    # pylint: disable=no-self-use
    def post(self):
        """Function to send link to mail"""
        email = request.json.get("email")
        username = request.json.get("username")
        if not email and not username:
            return {"message": "Email or username is required"}, 400
        user = db.session.query(User).filter(
            or_(User.username == username, User.email == email)).first()
        if not user:
            return {"message": "This user doesn't exist"}, 404
        if cache.get(f"reset_password:{user.uuid}"):
            print(f"reset_password:{user.uuid}")
            return {"message": "Link was already sent"}, 409
        token = encode_auth_token(user.uuid, LINK_EXPIRATION, user.is_admin)
        cache.add(f"reset_password:{user.uuid}", token,
                  timeout=int(timedelta(**LINK_EXPIRATION).total_seconds()))
        # TODO: don't hardcode
        send_email.apply_async(
            args=["Reset password", [user.email],
                  f"Send POST-request by the link "
                  f"http://localhost:5000/auth/set-password/{token} "
                  f"to change your password"])
        return {"message": "Link to change password was sent to your mail"}


class SetNewPasswordApi(Resource):
    """Class to se new password"""
    # pylint: disable=no-self-use
    def post(self, token: str):
        """Function to set new password"""
        new_password = request.json.get("password")
        if not new_password:
            return {"message": "Provide a new password"}, 400
        try:
            payload = decode_auth_token(token)
        except jwt.ExpiredSignatureError:
            return {"message": "The link is expired"}, 410
        except jwt.InvalidTokenError:
            return {"message": 'The link is invalid. Check if the link '
                               'was copied rightly'}, 400
        uuid = payload["sub"]
        if not cache.get(f"reset_password:{uuid}"):
            return {"message": "This link was already used"}
        user = db.session.query(User).filter_by(uuid=uuid).first()
        user.password = new_password
        user.save()
        cache.delete(f"reset_password:{uuid}")
        return {"message": "Password was successfully changed"}
