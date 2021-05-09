from sqlalchemy.orm import Query, Session

from library.models import Book


class BookServices:
    def __init__(self, query: Query):
        self.query = query

    def filter_by_category(self, categories: list):
        if categories:
            self.query = self.query.filter(Book.category.in_(categories))
        return self

    def filter_by_publisher(self, publishers: list):
        if publishers:
            self.query = self.query.filter(Book.publisher.in_(publishers))
        return self

    def filter_by_language(self, languages: list):
        if languages:
            self.query = self.query.filter(Book.language.in_(languages))
        return self

    def sort_by_title(self):
        self.query = self.query.order_by(Book.title.asc())
        return self

    def sort_by_price(self, order: str):
        if order == "asc":
            self.query = self.query.order_by(Book.price.asc())
        elif order == "desc":
            self.query = self.query.order_by(Book.price.desc())
        else:
            self.query = self.query.order_by(Book.title.asc())
        return self
