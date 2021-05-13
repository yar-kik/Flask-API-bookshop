"""Module for deserialization and serialization library models"""

import datetime
from marshmallow import fields, validate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .models import Book

START_YEAR = 2000


class BookSchema(SQLAlchemyAutoSchema):
    """Class for book model serialization/deserialization"""
    published = fields.Integer(required=False,
                               validate=validate.Range(
                                   START_YEAR, datetime.datetime.now().year))
    pages = fields.Integer(validate=validate.Range(1))
    price = fields.Float(required=True, validate=validate.Range(0))

    # pylint: disable=missing-class-docstring
    class Meta:
        model = Book
        dump_only = ('id',)
        load_instance = True
