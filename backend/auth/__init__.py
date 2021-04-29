from flask import Blueprint
from flask_restful import Api

auth = Blueprint('auth', __name__)
api = Api(auth)

from . import routes
