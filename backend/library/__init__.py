from flask import Blueprint
from flask_restful import Api

library = Blueprint('library', __name__)
api = Api(library)

# Щоб уникнути циклічного імпорту і задіяти ці урли
from . import routes
from . import views
