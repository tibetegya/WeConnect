import unittest
import flask 
import json
from apis import api
from run import app
from apis.v2.tests import ApiTestCase

class ReviewTestCase(ApiTestCase):
    """ Tests For the Reviews Endpoints """

    def test_get(self):
        """ Test that there are no business reviews """
        res = self.client().get('/businesses/1/reviews')
        self.assertEqual(res.status_code, 404 )

