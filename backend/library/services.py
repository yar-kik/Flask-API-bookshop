"""Module for book database services"""

from flask import current_app
from sqlalchemy import asc, desc
from sqlalchemy.orm import Query
from werkzeug.datastructures import ImmutableMultiDict

from library.models import Book


class BookServices:
    """Class to work with database"""

    ORDER = {"asc": asc, "desc": desc}
    SORT = {"price": Book.price, "published": Book.published}
    PARAMETERS = {"category": Book.category,
                  "publisher": Book.publisher,
                  "language": Book.language}

    def __init__(self, db_query: Query, search_query: ImmutableMultiDict):
        self.db_query = db_query
        self.search_query = search_query

    def filter_by_query(self):
        """Filter books by query parameters"""
        for param in self.search_query:
            if param in self.PARAMETERS:
                self.db_query = self.db_query.filter(
                    self.PARAMETERS[param].in_(
                        self.search_query.getlist(param)))
        return self

    def sort_by_query(self):
        """Sort books by query parameters"""
        order = self.search_query.get("order")
        sort = self.search_query.get("sort")
        if order in self.ORDER and sort in self.SORT:
            self.db_query = self.db_query.order_by(
                self.ORDER[order](self.SORT[sort]))
        else:
            self.db_query = self.db_query.order_by(Book.title.asc())
        return self

    def paginate_by_query(self):
        """Paginate books by page number"""
        page = self.search_query.get('page', 1, type=int)
        return self.db_query.paginate(page,
                                      current_app.config['BOOKS_PER_PAGE'],
                                      True)
