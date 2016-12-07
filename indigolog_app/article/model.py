from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now())

    def __init__(self, title, created_at):
        self.title = title
        self.created_at = created_at

    def __repr__(self):
        return '<Title %r>' % self.title
