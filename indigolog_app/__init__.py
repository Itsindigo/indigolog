import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

# Flask Extensions
db = SQLAlchemy()

# Import models so that they are registered with SQLAlchemy
from indigolog_app.article import model


def create_app(config_name=None, main=True):
    if config_name is None:
        config_name = os.environ.get('INDIGOLOG_CONFIG', 'development')

    indigolog = Flask(__name__)
    indigolog.config.from_object(config[config_name])

    db.init_app(indigolog)

    # Register web application routes
    from .indigolog import home as home_blueprint
    # from indigolog_app.article.views import article
    indigolog.register_blueprint(home_blueprint)

    return indigolog