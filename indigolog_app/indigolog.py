from flask import Flask

indigolog = Flask(__name__)


@indigolog.route('/')
def home():
    return 'Home page.'


if __name__ == '__main__':
    indigolog.run()
