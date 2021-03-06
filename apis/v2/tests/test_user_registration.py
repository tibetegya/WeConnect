import unittest

import flask
import json

from apis import app
from apis.v2.tests import ApiTestCase
from apis.v2.models.blacklist import Blacklist
from apis.v2.models.user import User


class UserTestCase(ApiTestCase):
    """ Tests For the Reviews Endpoints """


    def test_api_does_not_create_account_without_username(self):
        """tests that the api rejects a request to register a user without a username """

        res = self.client().post(self.base_url+self.user_register_endpoint,
                                data=json.dumps(self.other_users[2]),
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_api_does_not_create_account_with_empty_username(self):
        """ tests that api rejects a request to register a user with username that is an empty string """

        res = self.client().post(self.base_url+self.user_register_endpoint,
                                data=json.dumps(self.invalid_users['empty username']),
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_api_does_not_create_account_with_invalid_username(self):
        """ test that the api rejects invalid user names"""

        res = self.client().post(self.base_url+self.user_register_endpoint,
                                data=json.dumps(self.invalid_users['invalid username']),
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_api_does_not_create_account_with_long_username(self):
        """tests that the api rejects a request to register a user with username payload longer than the db model """

        res = self.client().post(self.base_url+self.user_register_endpoint,
                                data=json.dumps(self.invalid_users['long username']),
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_api_does_not_create_account_without_password(self):
        """ tests that the api rejects a request to register a user without a password """

        res = self.client().post(self.base_url+self.user_register_endpoint,
                                data=json.dumps(self.other_users[3]),
                                content_type='application/json')
        self.assertEqual(res.status_code, 400)


    def test_api_does_not_create_account_without_email(self):
        """tests that the api rejects a request to register a user without an email """

        res = self.client().post(self.base_url+self.user_register_endpoint,
                                data=json.dumps(self.other_users[4]),
                                content_type='application/json')
        self.assertEqual(res.status_code, 400)


    def test_api_does_not_create_account_with_empty_email(self):
        """ testa that the api  rejects a request to register a user with an empty string payload """

        self.other_users[0]['email']= ''
        res = self.client().post(self.base_url+self.user_register_endpoint,
                                data=json.dumps(self.other_users[0]),
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_api_does_not_create_account_with_invalid_email(self):
        """tests that the api rejects a request to register a user with an invalid email """

        res = self.client().post(self.base_url+self.user_register_endpoint,
                                data=json.dumps(self.invalid_users['invalid email']),
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_api_does_not_create_account_with_long_email(self):
        """tests that the api rejects a request to register a user with an email length longer than the db model """

        res = self.client().post(self.base_url+self.user_register_endpoint,
                                data=json.dumps(self.invalid_users['long email']),
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_api_does_not_create_account_with_an_empty_password(self):
        """tests that the api rejects a request to register a user with a password payload that is empty"""

        self.other_users[0]['password']= ''
        res = self.client().post(self.base_url+self.user_register_endpoint,
                                data=json.dumps(self.other_users[0]),
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_api_can_create_account(self):
        """ tests that the api can register a user """

        res = self.client().post(self.base_url+self.user_register_endpoint,
                                data=json.dumps(self.other_users[1]),
                                content_type='application/json')

        self.assertEqual(res.status_code, 201)


    def test_api_can_add_user_account_to_db(self):
        """ tests that the api can register a user """

        added_user = User.query.get(1)
        self.assertEqual('<User: {}>'.format(self.test_users[0]['user_name']), str(added_user))


    def test_api_can_not_create_account_for_existent_user(self):
        """tests that the api can not register an already existent user in the database """

        res = self.client().post(self.base_url+self.user_register_endpoint,
                                data=json.dumps(self.test_users[0]),
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_user_successfully_logs_in(self):
        """tests that the api can succefully log in a user """

        self.register_test_user(self.other_users[0])
        res = self.client().post(self.base_url+self.user_login_endpoint,
                                data=json.dumps(self.other_users[0]),
                                content_type='application/json')

        self.assertEqual(res.status_code, 200)


    def test_user_can_not_login_if_not_registered(self):
        """tests that the api can not login a user that is not registered """

        res = self.client().post(self.base_url+self.user_login_endpoint,
                                data=json.dumps(self.other_users[0]),
                                content_type='application/json')

        self.assertEqual(res.status_code, 403)


    def test_token_is_returned_upon_user_successfully_logs_in(self):
        """ tests that a token is returned when a user logs in """

        self.register_test_user(self.other_users[0])
        res = self.client().post(self.base_url+self.user_login_endpoint,
                                data=json.dumps(self.other_users[0]),
                                content_type='application/json')

        self.assertIn('token', str(res.data))


