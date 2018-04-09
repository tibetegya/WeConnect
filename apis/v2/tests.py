import unittest
from run import app
from apis.db import db


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app =app
        self.app.testing = True
        self.client = self.app.test_client
        self.base_url = '/api/v2'

        with self.app.app_context():
            db.session.close()
            db.drop_all()
            db.create_all()



    def tearDown(self):
        with self.app.app_context():
            db.session.close()
            db.drop_all()