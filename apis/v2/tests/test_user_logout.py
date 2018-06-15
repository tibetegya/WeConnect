import unittest

import flask
import json

from apis import app
from apis.v2.tests import ApiTestCase
from apis.v2.models.blacklist import Blacklist
from apis.v2.models.user import User


class UserTestCase(ApiTestCase):
    """ Tests For the Reviews Endpoints """


    def test_user_can_logout(self):
        """ tests that api can logout a user """

        res = self.client().post(self.base_url+self.user_logout_endpoint,
                                headers={'Authorization': 'Bearer ' + self.tokens[0]})

        self.assertEqual(res.status_code, 200)


    def test_token_is_blacklisted_on_logout(self):
        """ tests that api can blacklist token """

        res = self.client().post(self.base_url+self.user_logout_endpoint,
                                headers={'Authorization': 'Bearer ' + self.tokens[0]})
        blacklisted = Blacklist.query.all()
        self.assertEqual('<Token: {}'.format(self.tokens[0]), str(blacklisted[0]))



    def test_for_no_token(self):
        """ tests that api catches missing token"""

        res = self.client().post(self.base_url+self.user_logout_endpoint)

        self.assertEqual(res.status_code, 401)

    def test_for_invalid_token(self):
        """ tests that api catches an unthorised request"""

        res = self.client().post(self.base_url+self.user_logout_endpoint,
                                headers={'Authorization': 'Bearer {}'.format(self.post_token)})

        self.assertEqual(res.status_code, 401)

    def test_for_blacklisted_token(self):
        """ tests that api catches missing token"""
        # log out a user
        self.log_out_user(self.tokens[3])
        res = self.client().post(self.base_url+self.user_logout_endpoint,
                                headers={'Authorization': 'Bearer {}'.format(self.tokens[3])})

        self.assertEqual(res.status_code, 401)

    def test_for_missing_token(self):
        """ tests that api catches missing token"""

        res = self.client().post(self.base_url+self.user_logout_endpoint,
                                headers={'Authorization': 'Bearer'})

        self.assertEqual(res.status_code, 401)
