import unittest
import flask 
import json
from apis import api
from apis import app
from apis.v2.tests import ApiTestCase

class ReviewTestCase(ApiTestCase):
    """ Tests For the Reviews Endpoints """

    def test_get_all_reviews_for_a_business(self):

        #add a business
        res = self.client().post(self.base_url+self.business_list_endpoint, 
                        data=json.dumps(self.test_business),
                        content_type='application/json')

        #add review to business             
        res = self.client().post(self.base_url+self.review_endpoint, 
                        data=json.dumps(self.test_review),
                        content_type='application/json')

        
        res = self.client().get(self.base_url+self.review_endpoint)
        self.assertEqual(res.status_code, 200)

    def test_can_post_review(self):
        """ Test that api can post a  reviews """

        #add a business
        res = self.client().post(self.base_url+self.business_list_endpoint, 
                        data=json.dumps(self.test_business),
                        content_type='application/json')
        self.assertEqual(res.status_code, 201)  

        #add review to business             
        res = self.client().post(self.base_url+self.review_endpoint, 
                        data=json.dumps(self.test_review),
                        content_type='application/json')
        self.assertEqual(res.status_code, 201)


    def test_get_review_for_existing_business(self):
        """ Test that api can get a review/s for existing business"""

    def test_get_review_for_non_existing_business(self):
        """ Test that api can not get a review/s for non existing business"""
        res = self.client().get(self.base_url+self.review_endpoint)
        
        self.assertEqual(res.status_code, 404)