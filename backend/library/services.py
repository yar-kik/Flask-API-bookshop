from flask import current_app
from sqlalchemy import asc, desc
from sqlalchemy.orm import Query
from werkzeug.datastructures import ImmutableMultiDict

from library.models import Book


class BookServices:
    ORDER = {"asc": asc, "desc": desc}
    SORT = {"price": Book.price, "published": Book.published}
    PARAMETERS = {"category": Book.category,
                  "publisher": Book.publisher,
                  "language": Book.language}

    def __init__(self, query: Query):
        self.query = query

    def filter_by(self, parameters: ImmutableMultiDict):
        for param in parameters:
            if param and param in self.PARAMETERS:
                self.query = self.query.filter(
                    self.PARAMETERS[param].in_(parameters.getlist(param)))
        return self

    def sort_by(self, sort: str, order: str):
        if order in self.ORDER and sort in self.SORT:
            self.query = self.query.order_by(self.ORDER[order](self.SORT[sort]))
        else:
            self.query = self.query.order_by(Book.title.asc())
        return self

    def paginate_by(self, page: int):
        return self.query.paginate(page,
                                   current_app.config['BOOKS_PER_PAGE'], True)
