from . import api
from .views import BookApi, BookListApi

api.add_resource(BookListApi, '/books', strict_slashes=False)
api.add_resource(BookApi, '/books/<id>', strict_slashes=False)