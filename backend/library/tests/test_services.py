"""Module for testing book services"""

import unittest

from library.models import Book
from library.services import BookServices
from utils import db, create_app


class TestBookServices(unittest.TestCase):
    """Class for testing book services"""

    def setUp(self) -> None:
        """
        Define test variables and initialize app.
        """
        self.app = create_app("testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
        self.service = BookServices(db.session.query(Book))
        for i in range(10):
            book = Book(title=f"Book {i}",
                        author=f"Author {i}",
                        price=((i + 1) * 20))
            if i % 3 == 0:
                book.language = "russian"
                book.publisher = "O'Reilly"
                book.category = "fantasy"
            elif i % 3 == 1:
                book.language = "ukrainian"
                book.publisher = "Manning Publications"
                book.category = "detective"
            else:
                book.language = "english"
                book.publisher = "No Starch Press"
                book.category = "adventure"
            db.session.add(book)
            db.session.commit()
