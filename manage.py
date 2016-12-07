import os
import sys

from flask_script import Manager, Command, Server

from indigolog_app import create_app, db

manager = Manager(create_app)
manager.add_command("runserver", Server())

if __name__ == "__main__":
    manager.run()
