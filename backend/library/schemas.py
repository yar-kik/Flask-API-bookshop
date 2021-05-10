"""Module for deserialization and serialization library models"""

import datetime
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .models import Book

START_YEAR = 2000


def validate_year(year):
    """Function to validate published year"""
    return START_YEAR <= year <= datetime.datetime.now().year


class BookSchema(SQLAlchemyAutoSchema):
    """Class for book model serialization/deserialization"""
    published = fields.Int(required=False,
                           validate=validate_year)

    # pylint: disable=missing-class-docstring
    class Meta:
        model = Book
        dump_only = ('id',)
        load_instance = True
