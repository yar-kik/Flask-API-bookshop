import unittest
from library.models import Book


class TestBookModel(unittest.TestCase):
    def setUp(self) -> None:
        self.book = Book(title="book title", author="book author")

    def test_model_str(self):
        self.assertEqual(str(self.book), 'Book (book title), book author')
