"""Module for deserialization and serialization auth models"""
from marshmallow import fields, validate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .models import User


class UserSchema(SQLAlchemyAutoSchema):
    """Class for user model serialization/deserialization"""
    username = fields.String(required=True,
                             validate=[validate.Length(4, 32),
                                       validate.Regexp(
                                           r"^[a-zA-Z0-9_-]{4,32}$")])
    email = fields.Email(required=True, validate=validate.Length(max=64))
    password = fields.String(required=True,
                             validate=[validate.Length(4, 64),
                                       validate.Regexp(
                                           r"^[a-zA-Z0-9_!@#$%^&*-]{4,64}$")])

    # pylint: disable=missing-class-docstring
    class Meta:
        model = User
        exclude = ('id', 'uuid', 'is_admin')
        load_only = ('password',)
        load_instance = True
