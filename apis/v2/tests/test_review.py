import unittest

import flask
import json

from apis import app
from apis.v2.tests import ApiTestCase
from apis.v2.models.review import ReviewModel


class ReviewTestCase(ApiTestCase):
    """ Tests For the Reviews Endpoints """


    def test_get_all_reviews_for_a_business(self):
        """ Tests that Reviews Endpoint returns a review """

        res = self.client().get(self.base_url+self.review_endpoint)

        self.assertEqual(res.status_code, 200)


    def test_can_post_review(self):
        """ Test that api can post a review """

        res = self.client().post(self.base_url+self.review_endpoint2,
                                data=json.dumps(self.other_reviews[0]),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 201)

    def test_post_review_non_existent_business(self):
        """ Test that api can not post a review to non existent business"""

        res = self.client().post(self.base_url+self.review_endpoint_900,
                                data=json.dumps(self.other_reviews[0]),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_business_owner_can_not_post_review(self):
        """ Test that api rejects a review post from the business owner  """

        res = self.client().post(self.base_url+self.review_endpoint,
                                data=json.dumps(self.other_reviews[0]),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 403)

    def test_review_added_to_db(self):
        """ Test that api add a review to the database """

        added_review = ReviewModel.query.get(1)
        self.assertEqual('<Review: {}>'.format(self.test_reviews[0]['title']), str(added_review))


    def test_post_incomplete_review(self):
        """ Test that api can not post an incomplete review"""

        res = self.client().post(self.base_url+self.review_endpoint,
                                data=json.dumps(self.invalid_reviews[0]),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)

    def test_post_empty_review_title(self):
        """ Test that api can not post a review with an empty title"""

        res = self.client().post(self.base_url+self.review_endpoint,
                                data=json.dumps(self.invalid_reviews[3]),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)

    def test_post_empty_review_body(self):
        """ Test that api can not post a review with an empty body"""

        res = self.client().post(self.base_url+self.review_endpoint,
                                data=json.dumps(self.invalid_reviews[4]),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)

    def test_post_long_review_title(self):
        """ Test that api can not post a long reviews title"""

        res = self.client().post(self.base_url+self.review_endpoint,
                                data=json.dumps(self.invalid_reviews[1]),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_post_long_review_body(self):
        """ Test that api can post a long reviews body"""

        res = self.client().post(self.base_url+self.review_endpoint,
                                data=json.dumps(self.invalid_reviews[2]),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_cannot_post_review_without_token(self):
        """ Test that api can post a  reviews """

        res = self.client().post(self.base_url+self.review_endpoint,
                                data=json.dumps(self.other_reviews[0]),
                                content_type='application/json')

        self.assertEqual(res.status_code, 401)


    def test_get_review_for_non_existing_business(self):
        """ Test that api can not get a review/s for non existing business"""

        res = self.client().get(self.base_url+self.review_endpoint_900,
                                headers={'Authorization': 'Bearer ' + self.tokens[0]})

        self.assertEqual(res.status_code, 400)


    def test_error_handler(self):
        """ Test that api can not get a review/s for non existing business"""

        res = self.client().get(self.base_url+'fakeendpoint',
                                headers={'Authorization': 'Bearer ' + self.tokens[0]})

        self.assertEqual(res.status_code, 404)
