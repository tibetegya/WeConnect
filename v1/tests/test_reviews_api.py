import unittest
import flask 
import json
from v1 import api
from v1 import app
from ..tests import ApiTestCase

class ReviewTestCase(ApiTestCase):
    """ Tests For the Reviews Endpoints """

    def test_get(self):
        """ Test that there are no business reviews """
        res = self.client().get('/businesses/1/reviews')
        self.assertEqual(res.status_code, 404 )

