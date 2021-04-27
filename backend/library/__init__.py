from flask import Blueprint
from flask_restful import Api

main = Blueprint('main', __name__)
api = Api(main)

# Щоб уникнути циклічного імпорту і задіяти ці урли
from . import routes
from . import views