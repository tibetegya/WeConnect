import unittest
import flask 
import json
from apis import api
from apis import app
from apis.v2.tests import ApiTestCase

class ReviewTestCase(ApiTestCase):
    """ Tests For the Reviews Endpoints """

    def test_get_all_reviews_for_a_business(self):
        
        res = self.client().get(self.base_url+self.review_endpoint,
                        headers={'Authorization': 'Bearer ' + self.tokens[0]},)
        self.assertEqual(res.status_code, 200)

    def test_can_post_review(self):
        """ Test that api can post a  reviews """
        #add review to business             
        res = self.client().post(self.base_url+self.review_endpoint, 
                        data=json.dumps(self.other_reviews[0]),
                        headers={'Authorization': 'Bearer ' + self.tokens[0]},
                        content_type='application/json')
        self.assertEqual(res.status_code, 201)
    def test_post_incomplete_review(self):
        """ Test that api can not post an incomplete review"""
        #add review to business             
        res = self.client().post(self.base_url+self.review_endpoint, 
                        data=json.dumps(self.invalid_reviews[0]),
                        headers={'Authorization': 'Bearer ' + self.tokens[0]},
                        content_type='application/json')
        self.assertEqual(res.status_code, 403)

    def test_post_long_review_title(self):
        """ Test that api can not post a long reviews title"""
        #add review to business             
        res = self.client().post(self.base_url+self.review_endpoint, 
                        data=json.dumps(self.invalid_reviews[1]),
                        headers={'Authorization': 'Bearer ' + self.tokens[0]},
                        content_type='application/json')
        self.assertEqual(res.status_code, 400)
    
    def test_post_long_review_body(self):
        """ Test that api can post a long reviews body"""
        #add review to business             
        res = self.client().post(self.base_url+self.review_endpoint, 
                        data=json.dumps(self.invalid_reviews[2]),
                        headers={'Authorization': 'Bearer ' + self.tokens[0]},
                        content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_cannot_post_review_without_token(self):
        """ Test that api can post a  reviews """
        #add review to business             
        res = self.client().post(self.base_url+self.review_endpoint, 
                        data=json.dumps(self.other_reviews[0]),
                        content_type='application/json')
        self.assertEqual(res.status_code, 401)


    def test_get_review_for_non_existing_business(self):
        """ Test that api can not get a review/s for non existing business"""
        res = self.client().get(self.base_url+self.review_endpoint_900,
        headers={'Authorization': 'Bearer ' + self.tokens[0]})
        
        self.assertEqual(res.status_code, 400)