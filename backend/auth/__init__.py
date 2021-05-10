"""Init module"""

from flask import Blueprint
from flask_restful import Api

auth = Blueprint('auth', __name__)
api = Api(auth)

# pylint: disable=wrong-import-position
from . import routes
