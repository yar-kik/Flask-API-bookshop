"""Module for API routes"""

from . import api
from .views import RegisterApi, LoginApi, LogoutApi

api.add_resource(RegisterApi, '/registration', strict_slashes=False)
api.add_resource(LoginApi, '/login', strict_slashes=False)
api.add_resource(LogoutApi, '/logout', strict_slashes=False)
