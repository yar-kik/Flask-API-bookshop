"""Module for managing application"""

import os
from getpass import getpass
import re

from flask_migrate import MigrateCommand
from flask_script import Manager
from sqlalchemy.exc import IntegrityError

from auth.models import User
from utils import create_app, db

email_regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
username_regex = r"^[a-zA-Z0-9_-]{4,32}$"
app = create_app(os.getenv('FLASK_ENV') or 'default')
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def create_admin():
    username = input("Enter username: ")
    if not re.search(username_regex, username):
        return "Invalid username!"
    email = input("Enter email: ")
    if not re.search(email_regex, email):
        return "Invalid email!"
    for _ in range(3):
        password = getpass("Enter password: ")
        password2 = getpass("Enter password again: ")
        if password == password2:
            break
        print("Passwords are different!")
    else:
        return "Too many attempts. Try again"

    try:
        admin = User(username=username,
                     email=email,
                     password=password,
                     is_admin=True)
        db.session.add(admin)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return "User with this username or email already exists"
    return "Created successfully"


if __name__ == '__main__':
    manager.run()
