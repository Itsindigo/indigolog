from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
# from indigolog_app.article.views import article_blueprint

home = Blueprint('main', __name__)


@home.route('/')
def index():
    """Serve client-side application."""
    return 'HELLO WORLD.'
