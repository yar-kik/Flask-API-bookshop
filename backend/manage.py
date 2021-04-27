import os

from flask_script import Manager

from utils import create_app

app = create_app(os.getenv('FLASK_ENV') or 'default')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
