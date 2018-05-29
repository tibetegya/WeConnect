import unittest

import flask
import json

from apis import app
from apis.v2.tests import ApiTestCase
from apis.v2.models.business import BusinessModel


class BusinessListTestCase(ApiTestCase):
    """ Tests For the Businesses Endpoints """


    def test_get(self):

        res = self.client().get(self.base_url+self.business_list_endpoint,
                                headers={'Authorization': 'Bearer ' + self.tokens[0]})

        self.assertEqual(res.status_code, 200)


    def test_api_can_post_business(self):
        """ test that api can post a business """

        res = self.client().post(self.base_url+self.business_list_endpoint,
                                data=json.dumps(self.other_businesses[0]),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 201)


    def test_post_empty_category(self):
        """ test that api cannot post a business with empty category """
        self.other_businesses[0]['category'] = '  '
        res = self.client().post(self.base_url+self.business_list_endpoint,
                                data=json.dumps(self.other_businesses[0]),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)

    def test_post_empty_business_name(self):
        """ test that api cannot post a business with empty business name """
        self.other_businesses[0]['business_name'] = '  '
        res = self.client().post(self.base_url+self.business_list_endpoint,
                                data=json.dumps(self.other_businesses[0]),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)

    def test_api_can_add_business_db(self):
        """ test that api can add a business to the database"""

        added_business = BusinessModel.query.get(1)
        self.assertEqual('<Business: {}>'.format(self.test_businesses[0]['business_name']), str(added_business))


    def test_api_can_not_delete_non_existent_business(self):
        """ test that api can not delete a business that does not exist"""

        res = self.client().delete(self.base_url+self.business_endpoint_900,
                                    headers={'Authorization': 'Bearer ' + self.tokens[0]})

        self.assertEqual(res.status_code, 400)


    def test_api_can_delete_business(self):
        """ test that api can delete a business"""

        res = self.client().delete(self.base_url+self.business_endpoint_1,
                                    headers={'Authorization': 'Bearer ' + self.tokens[0]},)

        self.assertEqual(res.status_code, 201)

    def test_api_can_not_delete_business(self):
        """ test that api can not delete business if they donot own it delete a business"""

        res = self.client().delete(self.base_url+self.business_endpoint_1,
                                    headers={'Authorization': 'Bearer ' + self.tokens[1]},)

        self.assertEqual(res.status_code, 403)

    def test_api_can_return_a_specific_business(self):
        """ test that api can return a business when logged in """

        res = self.client().get(self.base_url+self.business_endpoint_2,
                                headers={'Authorization': 'Bearer ' + self.tokens[0]})

        self.assertEqual(res.status_code, 200)


    def test_api_cannot_return_a_business_when_not_logged_in(self):
        """ test that api can not return a business when not logged in"""

        res = self.client().get(self.base_url+self.business_endpoint_2)

        self.assertEqual(res.status_code, 401)


    def test_api_returns_nothing_with_businessId_larger_than_db(self):
        """ test that api rejects request with a business id that does not exist in the database"""
        res = self.client().get(self.base_url+self.business_endpoint_900,
                                headers={'Authorization': 'Bearer ' + self.tokens[0]})

        self.assertEqual(res.status_code, 400)


    def test_for_long_business_name_length(self):
        """ test that requests with long business names are rejected """

        res = self.client().post(self.base_url+self.business_list_endpoint,
                                data=json.dumps(self.invalid_businesses[0] ),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)

    def test_for_long_business_category_length(self):
        """ test that requests with long business categories are rejected """

        res = self.client().post(self.base_url+self.business_list_endpoint,
                                data=json.dumps(self.invalid_businesses[1] ),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_for_long_business_loaction_length(self):
        """ tests that requests with long business locations longer that business locations are rejected """

        res = self.client().post(self.base_url+self.business_list_endpoint,
                                data=json.dumps(self.invalid_businesses[2] ),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)

    def test_for_long_business_profile_length(self):
        """ tests that requests with profiles longer than db model are rejected """

        res = self.client().post(self.base_url+self.business_list_endpoint,
                                data=json.dumps(self.invalid_businesses[3] ),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)

    def test_api_rejects_post_business(self):
        """ test that api can reject posting an existent business """

        res = self.client().post(self.base_url+self.business_list_endpoint,
                                data=json.dumps(self.test_businesses[0]),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)

    def test_api_rejects_put_business(self):
        """ test that api can reject updating an existent business """

        res = self.client().put(self.base_url+self.business_endpoint_1,
                                data=json.dumps(self.test_businesses[2]),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)

    def test_search_string_works_(self):
        """ test that search string works """

        res = self.client().get(self.base_url+self.business_list_endpoint+
                    '?q=andela&location=gulu&category=appliances&limit=1&page=1',
                                data=json.dumps(self.test_businesses[1]),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 200)