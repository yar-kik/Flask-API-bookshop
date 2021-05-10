"""Init module"""

from flask import Blueprint
from flask_restful import Api

library = Blueprint('library', __name__)
api = Api(library)

# pylint: disable=wrong-import-position
from . import routes
