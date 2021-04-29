from datetime import datetime, timedelta

import jwt
from flask import request, current_app
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from auth.models import User
from auth.schemas import UserSchema
from utils import db


class AuthRegisterApi(Resource):
    user_schema = UserSchema()

    def post(self):
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
        return self.user_schema.dump(user), 201


class AuthLoginApi(Resource):
    def get(self):
        auth = request.authorization
        if not auth:
            return "", 401, \
                   {"WWW-Authenticate": "Basic realm='Authentication required'"}
        user = db.session.query(User).filter_by(username=auth.get("username", '')).first()
        if not user or not user.verify_password(auth.get("password", '')):
            return "", 401, \
                   {"WWW-Authenticate": "Basic realm='Authentication required'"}
        token = jwt.encode(
            {
                'user_id': user.uuid,
                'exp': datetime.now() + timedelta(hours=1)
            }, current_app.config['SECRET_KEY'], algorithm="HS256"
        )
        return {"token": token}, 200
