"""Module for different configurations such as 'production', 'development'
or 'testing.'"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configurations"""
    SECRET_KEY = os.environ.get('SECRET_KEY')

    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = os.environ.get('MAIL_PORT', '587')
    MAIL_USE_TLS = bool(os.environ.get('MAIL_USE_TL', '1'))
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'username')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'password')

    FLASK_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASK_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASK_ADMIN = os.environ.get('FLASKY_ADMIN', 'flask_admin')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BOOKS_PER_PAGE = os.environ.get('BOOKS_PER_PAGE', 5)

    CACHE_DEFAULT_TIMEOUT = os.environ.get("CACHE_DEFAULT_TIMEOUT", 60 * 60)

    @staticmethod
    def init_app(app):
        """Function for application initialization. It could be add
        some functionality in future"""


class DevelopmentConfig(Config):
    """Configurations for development"""
    CACHE_TYPE = os.environ.get("CACHE_TYPE") or "SimpleCache"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
                              "sqlite:///" + os.path.join(basedir,
                                                          'data-dev.sqlite')


class TestingConfig(Config):
    """Configurations for testing"""
    CACHE_TYPE = os.environ.get("CACHE_TYPE") or "NullCache"
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite://'


class ProductionConfig(Config):
    """Configurations for production"""
    CACHE_TYPE = os.environ.get("CACHE_TYPE") or "RedisCache"
    CACHE_REDIS_URL = os.environ.get("CACHE_REDIS_URL") or \
                      "redis://localhost:6379"
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URL") or \
                              "postgresql://postgres:postgres@localhost:5432/postgres"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
