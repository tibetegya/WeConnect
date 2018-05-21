import unittest
import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from apis import app, db
from apis.v2.models.blacklist import Blacklist
from apis.v2.models.business import BusinessModel
from apis.v2.models.review import ReviewModel
from apis.v2.models.user import User



migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def migrator():
    run = 'python manage.py  db'
    if not os.path.isdir('./migrations'):
        os.system('{} init'.format(run))
    os.system('{} migrate'.format(run))
    os.system('{} upgrade'.format(run))

@manager.command
def test():
    tests = unittest.TestLoader().discover('apis/v2', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    # if result.wasSuccessful() return 0 else 1
    # return the opposite boolean
    return not result.wasSuccessful()

if __name__ == '__main__':
    manager.run()