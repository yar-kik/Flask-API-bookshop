"""Module for API routes"""

from . import api
from .views import BookApi, BookListApi, SearchApi

api.add_resource(BookListApi, '/books', strict_slashes=False)
api.add_resource(BookApi, '/books/<book_id>', strict_slashes=False)
api.add_resource(SearchApi, '/books/search', strict_slashes=False)
