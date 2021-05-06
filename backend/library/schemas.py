from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .models import Book
import datetime

START_YEAR = 2000


def validate_year(x):
    return START_YEAR <= x <= datetime.datetime.now().year


class BookSchema(SQLAlchemyAutoSchema):
    published = fields.Int(required=False,
                           validate=validate_year)

    class Meta:
        model = Book
        dump_only = ('id',)
        load_instance = True
