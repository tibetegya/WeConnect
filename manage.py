import unittest
from flask_script import Manager
from run import app

manager = Manager(app)

@manage.command
def migrator():
    os.system('set FLASK_APP=run')
        
    os.system('flask db init')
    # os.system('flask db migrate')
    # os.system('flask db upgrade')

@manager.command
def test():
    tests = unittest.TestLoader().discover('./v1/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    # if result.wasSuccessful() return 0 else 1
    # return the opposite boolean
    return not result.wasSuccessful()

if __name__ == '__main__':
    manager.run()