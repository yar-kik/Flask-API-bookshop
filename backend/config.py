"""Module for different configurations such as 'production', 'development'
or 'testing.'"""

import os
from dotenv import load_dotenv

load_dotenv(".env.local")
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Base configurations"""
    SECRET_KEY = os.environ.get('SECRET_KEY', "hardtorememberstring")

    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = os.environ.get('MAIL_PORT', '587')
    MAIL_USE_TLS = bool(int(os.environ.get('MAIL_USE_TLS', '1')))
    MAIL_USE_SSL = bool(int(os.environ.get('MAIL_USE_SSL', '0')))
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    FLASK_MAIL_SENDER = "flask@mail.com"
    ADMINS = ["admin@mail.com"]

    CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL",
                                       'redis://localhost:6379')
    CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND",
                                           'redis://localhost:6379')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    BOOKS_PER_PAGE = os.environ.get('BOOKS_PER_PAGE', 5)
    SEARCH_RESULT_PER_PAGE = os.environ.get("SEARCH_RESULT_PER_PAGE", 5)

    CACHE_DEFAULT_TIMEOUT = os.environ.get("CACHE_DEFAULT_TIMEOUT", 60 * 60)

    @staticmethod
    def init_app(app):
        """Function for application initialization. It could be add
        some functionality in future"""


class DevelopmentConfig(Config):
    """Configurations for development"""
    CACHE_TYPE = os.environ.get("DEV_CACHE_TYPE") or "SimpleCache"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
                              "sqlite:///" + os.path.join(basedir,
                                                          'data-dev.sqlite')


class TestingConfig(Config):
    """Configurations for testing"""
    CACHE_TYPE = os.environ.get("TEST_CACHE_TYPE") or "NullCache"
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite://'


class ProductionConfig(Config):
    """Configurations for production"""
    CACHE_TYPE = os.environ.get("PROD_CACHE_TYPE") or "RedisCache"
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

