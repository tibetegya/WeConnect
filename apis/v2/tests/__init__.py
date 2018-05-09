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
        self.business_endpoint_1 = '/businesses/1'
        self.business_endpoint_2 = '/businesses/2'
        self.business_endpoint_one = '/businesses/one'
        self.business_endpoint_900 = '/businesses/900'
        
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
        
        self.other_users = [ { 'user_name': 'sonia', 'email': 'sonia@andela.com', 'password': 'karungi'},
                            {'user_name': 'elijah', 'email': 'elijah@andela.com', 'password': 'rwothoromo'},
                            {'email': 'roger@andela.com', 'password': 'okello'},
                            {'user_name': 'elijah', 'email': 'elijah@andela.com'},
                            {'user_name': 'elijah', 'password': 'karungi'}
                        ]
        
        self.reset_george_password = {'current_password': 'tibetegya','new_password': 'tibzy'}

        self.test_businesses = [ {'business_name': 'airtel','category': 'telcom','location': 'kampala','profile': 'airtel profile' },
                                 {'business_name': 'safe boda','category': 'transport','location': 'kampala','profile': 'safe boda profile' },
                                 {'business_name': 'mtn','category': 'telcom','location': 'kampala','profile': 'mtn profile' },
                                 {'business_name': 'andela','category': 'software','location': 'gulu','profile': 'andela profile' } ]
        
        self.other_businesses = [ {'business_name': 'vodafone','category': 'cellular','location': 'gulu','profile': 'vodafone profile' },
                                 {'business_name': 'apple','category': 'appliances','location': 'gulu','profile': 'apple profile' } ]

        self.invalid_businesses = [ {'business_name': 'vodafonevodafonevodafonevodafonevodafonevodafonevodafonevodafonevodafone',
                                    'category': 'cellular','location': 'gulu','profile': 'vodafone profile' },
                                    {'business_name': 'vodafone','category': 'cellularcellularcellularcellularcellularcellularcellularcellular',
                                    'location': 'gulu','profile': 'vodafone profile' },
                                    {'business_name': 'vodafone','category': 'cellular',
                                    'location': 'guluguluguluguluuluguluguluguluuluguluguluguluulugulugulugulu','profile': 'vodafone profile' },
                                    {'business_name': 'apple','category': 'appliances','location': 'gulu',
                                    'profile': 'apple profileapple profileapple profileapple profileapple profileapple profileapple profile\
                                        apple profileapple profileapple profileapple profileapple profileapple profileapple profile\
                                        apple profileapple profileapple profileapple profileapple profileapple profileapple profile' } ]

        self.review_endpoint = '/businesses/1/reviews'
        self.review_endpoint_900 = '/businesses/900/reviews'
        self.test_reviews = [{'title': 'Work with them', 'body': 'This is a great establishment'},
                             {'title': 'they are the best', 'body': 'This is a great establishment of proffesional;s'},
                             {'title': 'quality guaranteed', 'body': 'You wont be dis appointed because This is a great establishment'}]
        
        self.other_reviews = [{'title': 'excellent', 'body': 'This is a great establishment'},
                             {'title': 'super', 'body': 'This is a great establishment of proffesional;s'}]
        
        self.invalid_reviews = [{'title': 'super'},
                                {'title': 'excellentexcellentexcellentexcellentexcellentxcellentexcellentexcellentexcellentexcellent',
                                 'body': 'This is a great establishment'},
                             {'title': 'super', 
                             'body': 'This is a great establishment of proffesionalshis is a great establishment of proffesionals\
                                This is a great establishment of proffesionalshis is a great establishment of proffesionals\
                                This is a great establishment of proffesionalshis is a great establishment of proffesionals\
                                This is a great establishment of proffesionalshis is a great establishment of proffesionals'}]
        
        self.tokens = []
        # REGISTER AND LOGIN USERS
        for user in self.test_users:
            self.register_test_user(user)
            self.tokens.append(self.login_test_user(user))
        
        # REGISTER BUSINESSES
        for i in range(3):
            self.register_test_businesses(self.test_businesses[i], self.tokens[i])

        # Add reviews to a business
        for review in self.test_reviews:
            self.add_test_reviews(review, self.tokens[0])


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

    def register_test_businesses(self, business, token):
            res = self.client().post(self.base_url+self.business_list_endpoint, 
                        data=json.dumps(business),
                        headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')

    def add_test_reviews(self, review, token):
            res = self.client().post(self.base_url+self.review_endpoint, 
                        data=json.dumps(review),
                        headers={'Authorization': 'Bearer ' + token},
                        content_type='application/json')
              