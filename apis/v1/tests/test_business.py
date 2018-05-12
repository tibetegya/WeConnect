import unittest

import flask
import json

from apis import app
from apis import  api
from apis.v1.tests import ApiTestCase


class BusinessListTestCase(ApiTestCase):
    """ Tests For the Businesses Endpoints """

 

    def test_api_can_post_business(self):
        """ test that api can post a business """

        res = self.client().post(self.base_url+self.business_list_endpoint, 
                    data=json.dumps(self.test_business),
                    content_type='application/json')
        
        self.assertEqual(res.status_code, 201 )

    def test_api_can_update_business(self):
        """ test that api can update a business """
        res = self.client().post(self.base_url+self.business_list_endpoint, 
                    data=json.dumps(self.test_business),
                    content_type='application/json')
        
        self.assertEqual(res.status_code, 201 )
        self.test_business['location']= 'gulu'
        res = self.client().put(self.base_url+self.business_endpoint, 
                    data=json.dumps(self.test_business),
                    content_type='application/json')
        
        self.assertEqual(res.status_code, 201 )

    def test_api_can_not_update_non_existent_business(self):
        """ test that api can not update a business that does not exist"""
        res = self.client().post(self.base_url+self.business_list_endpoint, 
                    data=json.dumps(self.test_business),
                    content_type='application/json')
        
        self.assertEqual(res.status_code, 201 )
        self.test_business['location']= 'gulu'
        res = self.client().put(self.base_url+self.business_endpoint2, 
                    data=json.dumps(self.test_business),
                    content_type='application/json')
        
        self.assertEqual(res.status_code, 404 )


    def test_api_can_not_delete_non_existent_business(self):
        """ test that api can not delete a business that does not exist"""
        res = self.client().delete(self.base_url+self.business_endpoint)
        self.assertEqual(res.status_code, 400 )

    def test_api_can_delete_business(self):
        """ test that api can delete a business"""
        res = self.client().post(self.base_url+self.business_list_endpoint, 
                    data=json.dumps(self.test_business),
                    content_type='application/json')
        
        res = self.client().delete(self.base_url+self.business_endpoint)
        self.assertEqual(res.status_code, 201 )

    def test_api_can_not_delete_non_integer_id(self):
        """ test that api can not delete a business using a non integer id in url"""
        res = self.client().post(self.base_url+self.business_list_endpoint, 
                    data=json.dumps(self.test_business),
                    content_type='application/json')

        res = self.client().delete(self.base_url+self.business_endpoint_one)
        self.assertEqual(res.status_code, 404 )