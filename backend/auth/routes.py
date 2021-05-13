"""Module for API routes"""

from . import api
from .views import AuthRegisterApi, AuthLoginApi

api.add_resource(AuthRegisterApi, '/registration', strict_slashes=False)
api.add_resource(AuthLoginApi, '/login', strict_slashes=False)
