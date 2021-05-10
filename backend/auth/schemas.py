"""Module for deserialization and serialization auth models"""

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .models import User


class UserSchema(SQLAlchemyAutoSchema):
    """Class for user model serialization/deserialization"""
    # pylint: disable=missing-class-docstring
    class Meta:
        model = User
        exclude = ('id', 'uuid', 'is_admin')
        load_only = ('password',)
        load_instance = True
