import unittest
import json
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


        self.test_users = [ { 'user_name': 'george', 'email': 'george@andela.com', 'password': 'tibetegya'},
                            { 'user_name': 'peter', 'email': 'peter@andela.com', 'password': 'walugembe'},
                            { 'user_name': 'ben', 'email': 'ben@andela.com', 'password': 'asiimwe'},
                            { 'user_name': 'david', 'email': 'david@andela.com', 'password': 'ssali'}
                        ]
        
        self.reset_george_password = {
            'current_password': 'tibetegya',
            'new_password': 'tibzy'}

        self.review_endpoint = '/businesses/1/reviews'
        self.test_review = { 'title': 'Work with them', 'body': 'This is a great establishment'}
        
        self.tokens = []
        # REGISTER AND LOGIN USERS
        for user in self.test_users:
            self.register_test_user(user)
            self.tokens.append(self.login_test_user(user))
            

    def tearDown(self):
        with self.app.app_context():
            db.session.close()
            db.drop_all()

    def register_test_user(self, tester):
        res = self.client().post(self.base_url+self.user_register_endpoint, 
                data=json.dumps(tester),
                content_type='application/json')


    def login_test_user(self, tester):
            res = self.client().post(self.base_url+self.user_login_endpoint, 
                        data=json.dumps(tester),
                        content_type='application/json')
            token_dict = json.loads(res.data.decode())
            token = token_dict['token']
            return token 