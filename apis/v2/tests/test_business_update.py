import unittest

import flask
import json

from apis import app
from apis.v2.tests import ApiTestCase
from apis.v2.models.business import BusinessModel

class BusinessListTestCase(ApiTestCase):
    """ Tests For the Businesses Endpoints """


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

        self.assertEqual(res.status_code, 400)

    def test_update_business_user_does_not_own(self):
        """ tests that a user can not update a business they do not own """

        res = self.client().put(self.base_url+self.business_endpoint_1,
                                data=json.dumps(self.other_businesses[0] ),
                                headers={'Authorization': 'Bearer ' + self.tokens[1]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 403)

    def test_api_cannot_update_business_name_that_exists(self):
        """ tests that api can not update a business to a business name that is used by another business """

        res = self.client().put(self.base_url+self.business_endpoint_1,
                                data=json.dumps(self.other_businesses[2] ),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

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


    def test_api_can_update_business(self):
        """ test that api can update a business """

        res = self.client().put(self.base_url+self.business_endpoint_1,
                                data=json.dumps(self.other_businesses[1]),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 201)

    def test_api_can_not_update_business(self):
        """ test that api can not update a business if they send no data"""

        res = self.client().put(self.base_url+self.business_endpoint_1,
                                data=json.dumps({}),
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)

    def test_api_can_not_update_non_existent_business(self):
        """ test that api can not update a business that does not exist"""

        res = self.client().put(self.base_url+self.business_endpoint_900,
                                headers={'Authorization': 'Bearer ' + self.tokens[0]},
                                data=json.dumps(self.test_businesses[0]),
                                content_type='application/json')

        self.assertEqual(res.status_code, 400)