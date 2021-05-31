"""Module for application utilities"""
from elasticsearch import Elasticsearch
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from config import config

db = SQLAlchemy()
migrate = Migrate(compare_type=True)
cache = Cache()


def create_app(config_name) -> Flask:
    """Function to create a Flask application"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    elasticsearch_url = app.config["ELASTICSEARCH_URL"]
    app.elasticsearch = Elasticsearch(elasticsearch_url) \
        if elasticsearch_url else None
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)

    from library import library
    from auth import auth
    app.register_blueprint(library)
    app.register_blueprint(auth, url_prefix="/auth")

    # pylint: disable=unused-import
    from library.models import Book
    from auth.models import User

    return app
