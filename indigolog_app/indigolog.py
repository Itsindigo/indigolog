from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from indigolog_app.home.home import home_blueprint

indigolog = Flask(__name__)
indigolog.register_blueprint(home_blueprint)
indigolog.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/indigolog-dev'
db = SQLAlchemy(indigolog)


if __name__ == '__main__':
    indigolog.run()
