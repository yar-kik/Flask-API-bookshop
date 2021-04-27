from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .models import Book


class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        dump_only = ['id']
        load_instance = True
