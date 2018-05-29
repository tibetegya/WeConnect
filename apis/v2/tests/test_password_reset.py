import unittest

import flask
import json

from apis import app
from apis.v2.tests import ApiTestCase
from apis.v2.models.blacklist import Blacklist
from apis.v2.models.user import User


class UserTestCase(ApiTestCase):
    """ Tests For the Reviews Endpoints """

    def test_user_can_reset_password(self):
        """tests that the api can reset a users password. """

        res = self.client().post(self.base_url+self.user_reset_password_endpoint,
                                data=json.dumps(self.reset_payload['both']),
                                headers={'Authorization': 'Bearer {}'.format(self.tokens[0]) },
                                content_type='application/json')

        self.assertEqual(res.status_code, 201)


    def test_reset_with_wrong_email(self):
        """tests that the api can not reset a users password with wrong email. """

        res = self.client().post(self.base_url+self.user_reset_password_endpoint,
                                data=json.dumps(self.reset_payload['wrong_email']),
                                headers={'Authorization': 'Bearer {}'.format(self.tokens[0]) },
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)

    def test_user_cannot_reset_password_with_no_payload(self):
        """tests that the api rejects password reset payload that is empty """

        res = self.client().post(self.base_url+self.user_reset_password_endpoint,
                                data=json.dumps(self.reset_payload['none']),
                                headers={'Authorization': 'Bearer {}'.format(self.tokens[0]) },
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_user_cannot_reset_password_with_missing_new_payload(self):
        """ tests that the api rejects a request with payload missing the new password """

        res = self.client().post(self.base_url+self.user_reset_password_endpoint,
                                data=json.dumps(self.reset_payload['only old']),
                                headers={'Authorization': 'Bearer {}'.format(self.tokens[0]) },
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_user_cannot_reset_password_with_missing_old_payload(self):
        """" tests that the api rejects a request with payload missing the new password """

        res = self.client().post(self.base_url+self.user_reset_password_endpoint,
                                data=json.dumps(self.reset_payload['only new']),
                                headers={'Authorization': 'Bearer {}'.format(self.tokens[0]) },
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_user_cannot_reset_password_with_empty_old_payload(self):
        """ tests that the api rejects a request with old password payload that is empty """

        res = self.client().post(self.base_url+self.user_reset_password_endpoint,
                                data=json.dumps(self.reset_payload['empty old']),
                                headers={'Authorization': 'Bearer {}'.format(self.tokens[0]) },
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_user_cannot_reset_password_with_empty_new_payload(self):
        """ tests that api rejects a request with new password payload that is an empty string """

        res = self.client().post(self.base_url+self.user_reset_password_endpoint,
                                data=json.dumps(self.reset_payload['empty new']),
                                headers={'Authorization': 'Bearer {}'.format(self.tokens[0]) },
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)

