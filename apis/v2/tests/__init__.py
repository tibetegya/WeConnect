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
        self.business_endpoint2 = '/businesses/2'
        self.business_endpoint_one = '/businesses/one'
        self.fake_business_endpoint = '/businesses/900'
        
        self.test_business = {
                'business_name': 'airtel',
                'category': 'telcom',
                'location': 'kampala',
                'profile': 'photo' }
        self.test_business_to_update = {
                'business_name': 'mtn',
                'category': 'carrier',
                'location': 'gulu',
                'profile': 'pic'}
        
        self.user_register_endpoint = '/auth/register'
        self.user_login_endpoint = '/auth/login'
        self.user_logout_endpoint = '/auth/logout'
        self.user_reset_password_endpoint = '/auth/reset-password'

        self.test_user = {
            'user_name': 'george256',
            'email': 'george@andela.com',
            'password': 'asdfgh123'}

        self.test_user_login = {
            'user_name': 'george256',
            'password': 'asdfgh123'}

        self.test_password_change = {
            'current_password': 'asdfgh123',
            'new_password': 'abcdefghj123'}

        self.review_endpoint = '/businesses/1/reviews'
        self.test_review = {
            'title': 'Work with them',
            'body': 'This is a great establishment',
            'author': 'george'}

        

    def tearDown(self):
        with self.app.app_context():
            db.session.close()
            db.drop_all()