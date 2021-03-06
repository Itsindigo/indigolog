from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class Article(db.Model):
    __name__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Title %r>' % self.title
