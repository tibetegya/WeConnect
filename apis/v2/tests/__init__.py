import unittest
from apis import app, db
from config import Config, app_config


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app =app
        app.config.from_object(app_config['testing'])
        self.app.testing = True
        self.client = self.app.test_client
        self.base_url = '/api/v2'
        db.create_all()
        self.business_list_endpoint = '/businesses'
        self.business_endpoint = '/businesses/1'
        self.fake_business_endpoint = '/businesses/900'
        
        self.test_business = {
                'business_name': 'airtel',
                'category': 'telcom',
                'location': 'kampala',
                'profile': 'photo'
        }



    def tearDown(self):
        with self.app.app_context():
            db.session.close()
            db.drop_all()