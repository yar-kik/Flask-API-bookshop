"""Module for auth controllers (views)"""

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError

from auth.models import User
from auth.schemas import UserSchema
from auth.services import encode_auth_token
from utils import db


class AuthRegisterApi(Resource):
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
        except IntegrityError as e:
            db.session.rollback()
            return {"message": "Such user exists"}, 409
        return {"user": self.user_schema.dump(user),
                "message": "Successfully registered"}, 201


class AuthLoginApi(Resource):
    """Class for user login"""

    # pylint: disable=no-self-use
    def post(self):
        """Function for user login"""
        auth = request.authorization
        if not auth:
            return {"message": "Authentication required"}, 401
        username = auth.get("username", '')
        user = db.session.query(User).filter(
            or_(User.username == username, User.email == username)).first()
        if not user or not user.verify_password(auth.get("password", '')):
            return {"message": "User doesn't exist or wrong password"}, 404
        token = encode_auth_token(user.uuid)
        return {"message": "Successfully logged in",
                "token": token}, 200
