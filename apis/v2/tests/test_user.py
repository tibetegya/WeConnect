import unittest
import flask 
import json
from apis import api
from apis import app
from apis.v2.tests import ApiTestCase


class UserTestCase(ApiTestCase):
    """ Tests For the Reviews Endpoints """
    # def register_test_user(self, tester):
    #     res = self.client().post(self.base_url+self.user_register_endpoint, 
    #             data=json.dumps(tester),
    #             content_type='application/json')


    # def login_test_user(self, tester_login):
    #         res = self.client().post(self.base_url+self.user_login_endpoint, 
    #                     data=json.dumps(tester_login),
    #                     content_type='application/json')
    #         token_dict = json.loads(res.data.decode())
    #         token = token_dict['token']
    #         return token 

    # def test_api_does_not_create_account_with_empty_username(self):
    #     self.test_user['user_name']= ''
    #     res = self.client().post(self.base_url+self.user_register_endpoint, 
    #                     data=json.dumps(self.test_user),
    #                     content_type='application/json')
    #     self.assertEqual(res.status_code, 403)

    # def test_api_does_not_create_account_with_empty_email(self):
    #     self.test_user['email']= ''
    #     res = self.client().post(self.base_url+self.user_register_endpoint, 
    #                     data=json.dumps(self.test_user),
    #                     content_type='application/json')
    #     self.assertEqual(res.status_code, 403)

    # def test_api_does_not_create_account_with_an_empty_password(self):
    #     self.test_user['password']= ''
    #     res = self.client().post(self.base_url+self.user_register_endpoint, 
    #                     data=json.dumps(self.test_user),
    #                     content_type='application/json')
    #     self.assertEqual(res.status_code, 403)

    # def test_api_can_create_account(self):
        
    #     res = self.client().post(self.base_url+self.user_register_endpoint, 
    #                     data=json.dumps(self.test_user),
    #                     content_type='application/json')
    #     self.assertEqual(res.status_code, 201)

    # def test_api_can_not_create_account_for_existent_user(self):
        
    #     res = self.client().post(self.base_url+self.user_register_endpoint, 
    #                     data=json.dumps(self.test_user),
    #                     content_type='application/json')
         
    #     res = self.client().post(self.base_url+self.user_register_endpoint, 
    #                     data=json.dumps(self.test_user),
    #                     content_type='application/json')
    #     self.assertEqual(res.status_code, 403) 

    # def test_user_successfully_logs_in(self):
    #     res = self.client().post(self.base_url+self.user_register_endpoint, 
    #                     data=json.dumps(self.test_user),
    #                     content_type='application/json')

    #     res = self.client().post(self.base_url+self.user_login_endpoint, 
    #                     data=json.dumps(self.test_user_login),
    #                     content_type='application/json')
    #     self.assertEqual(res.status_code, 200)
    
    # def test_user_can_not_login_if_not_registered(self):

    #     res = self.client().post(self.base_url+self.user_login_endpoint, 
    #                     data=json.dumps(self.test_user_login),
    #                     content_type='application/json')
    #     self.assertEqual(res.status_code, 404)

    def test_token_is_returned_upon_user_successfully_logs_in(self):
        self.register_test_user(self.other_users[0])
        res = self.client().post(self.base_url+self.user_login_endpoint, 
                        data=json.dumps(self.other_users[0]),
                        content_type='application/json')
        
        self.assertIn('token', str(res.data))

    def test_user_can_logout(self):

        res = self.client().post(self.base_url+self.user_logout_endpoint, 
                        headers={'Authorization': 'Bearer ' + self.tokens[0]})
        self.assertEqual(res.status_code, 200)


    def test_user_can_reset_password(self):

        res = self.client().post(self.base_url+self.user_reset_password_endpoint,
                        data=json.dumps(self.reset_george_password),
                        headers={'Authorization': 'Bearer {}'.format(self.tokens[0]) },
                        content_type='application/json')
        print(res.data)
        self.assertEqual(res.status_code, 201)

          
    