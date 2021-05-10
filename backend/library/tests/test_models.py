"""Module for testing library database model"""

import unittest
from library.models import Book


class TestBookModel(unittest.TestCase):
    """Class for testing book model"""

    def setUp(self) -> None:
        """Setting up test database and configs"""
        self.book = Book(title="book title", author="book author")

    def test_model_str(self) -> None:
        """Test book model representation"""
        self.assertEqual(str(self.book), 'Book (book title), book author')
