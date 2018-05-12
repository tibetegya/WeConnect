import unittest

import flask
import json

from apis import app
from apis import  api
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


    def test_api_can_update_business(self):
        """ test that api can update a business """

        res = self.client().put(self.base_url+self.business_endpoint_1,
                                data=json.dumps(self.other_businesses[1]),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 201)


    def test_api_can_not_update_non_existent_business(self):
        """ test that api can not update a business that does not exist"""

        res = self.client().put(self.base_url+self.business_endpoint_900,
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                data=json.dumps(self.test_businesses[0]),
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


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


    def test_business_location_is_changed(self):
        """ testing that the location can be changed """

        self.client().put(self.base_url+self.business_endpoint_1,
                            data=json.dumps(self.other_businesses[0] ),
                            headers={'Authorization': 'Bearer ' + self.tokens[0]},
                            content_type='application/json')
        business_changed = BusinessModel.query.get(1)

        self.assertEqual(business_changed.location, 'gulu')


    def test_business_name_is_changed(self):
        """ test that business name can be changed """

        self.client().put(self.base_url+self.business_endpoint_1,
                            data=json.dumps(self.other_businesses[0] ),
                            headers={'Authorization': 'Bearer ' + self.tokens[0]},
                            content_type='application/json')
        business_changed = BusinessModel.query.get(1)

        self.assertEqual(business_changed.business_name, 'vodafone')


    def test_business_category_is_changed(self):
        """ test that the busoness category can be changed """

        self.client().put(self.base_url+self.business_endpoint_1,
                        data=json.dumps(self.other_businesses[0] ),
                        headers={'Authorization': 'Bearer ' + self.tokens[0]},
                        content_type='application/json')
        business_changed = BusinessModel.query.get(1)

        self.assertEqual(business_changed.category, 'cellular')


    def test_business_profile_is_changed(self):
        """ testing that an api can change the profile """

        self.client().put(self.base_url+self.business_endpoint_1,
                            data=json.dumps(self.other_businesses[0] ),
                            headers={'Authorization': 'Bearer ' + self.tokens[0]},
                            content_type='application/json')
        business_changed = BusinessModel.query.get(1)

        self.assertEqual(business_changed.profile, 'vodafone profile')


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

    def test_for_long_business_name_update_length(self):
        """tests that business update requests with a business name longer than db model are rejected """

        res = self.client().put(self.base_url+self.business_endpoint_1,
                                data=json.dumps(self.invalid_businesses[0] ),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_for_long_business_category_update_length(self):
        """ tests that business update requests with a business category longer than db model are rejected """

        res = self.client().put(self.base_url+self.business_endpoint_1,
                                data=json.dumps(self.invalid_businesses[1] ),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_for_long_business_location_update_length(self):
        """tests that business update requests with a location length longer than db model are rejected """

        res = self.client().put(self.base_url+self.business_endpoint_1,
                                data=json.dumps(self.invalid_businesses[2] ),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)


    def test_for_long_business_profile_update_length(self):
        """ tests that a business update requests with a profile length longer than db model are rejected """

        res = self.client().put(self.base_url+self.business_endpoint_1,
                                data=json.dumps(self.invalid_businesses[3] ),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400 )
