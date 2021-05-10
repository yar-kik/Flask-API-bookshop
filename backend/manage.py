"""Module for managing application"""

import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from utils import create_app

app = create_app(os.getenv('FLASK_ENV') or 'default')
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
