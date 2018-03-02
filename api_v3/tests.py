import unittest
import flask 
import json
from datetime import datetime
from api_v3 import api, app
from api_v3.weconnect_api import Business, BusinessList, Review, businesses, reviews

class ApiTestCase(unittest.TestCase):
    
    def setUp(self):
        self.api =api
        self.app =app
        self.app.testing = True
        self.client = self.app.test_client
        self.base_url = '/api/v3'

        self.businesses = businesses
        self.my_business_list = BusinessList()
        self.business_list_endpoint = self.base_url +'/businesses'
        
        self.test_business = {'business_name':'airtel',
                            'id':1,
                            'category': 'tech',
                            'profile': 'pic',
                             }

        
        self.my_business = Business()
        self.business_endpoint = self.base_url +'/businesses/1'
        self.fake_business_endpoint = self.base_url +'/businesses/4'


        self.reviews = reviews
        self.my_review = Review()
        self.test_review = {'title':'airtel',
                            'id':1,
                            'body': 'tech',
                            'business': 'airtel',
                            'creation_date': datetime.now,
                            'author':'george' }
        

        
        

        
        



class BusinessListTestCase(ApiTestCase):
    """ Tests For the Businesses Endpoints """

    def test_get(self):
        res = self.client().get(self.business_list_endpoint)
        
        self.assertEqual(res.status_code, 200 )


    
    with app.test_request_context():
        def test_post(self):
            res = self.client().post(self.business_list_endpoint, 
                        data=json.dumps(self.test_business),
                        content_type='application/json')
            data = json.loads(res.get_data())
            self.assertEqual(res.status_code, 201 )

    with app.test_request_context():
        def test_business_added_name_on_post(self):
            res = self.client().post(self.business_list_endpoint, 
                        data=json.dumps(self.test_business),
                        content_type='application/json')
            data = json.loads(res.get_data())
            self.assertEqual(data['business_name']  , 'airtel')

        def test_delete(self):
            pass



class BusinessTestCase(ApiTestCase):
    """ Tests For the Single Business Methods and Endpoints  """


    def test_get(self):
        """ Test For that businesses are retrieved  """

        res = self.client().get(self.business_endpoint)
        self.assertEqual(res.status_code, 200 )



    def test_put(self):
        """ Test For the Single Business has been added  """


        res = self.client().put(self.business_endpoint, 
                        data=json.dumps(self.test_business),
                        content_type='application/json')
        self.assertEqual(res.status_code, 201)


    def test_put_bad_request(self):
        """ Test For the Single Businessid that is out of range  """

        res = self.client().put(self.fake_business_endpoint, 
                        data=json.dumps(self.test_business),
                        content_type='application/json')
        self.assertEqual(res.status_code, 400)



    
   


class ReviewTestCase(ApiTestCase):
    """ Tests For the Reviews Endpoints """

    def test_get(self):
        """ Test that there are no business reviews """
        res = self.client().get('/businesses/1/reviews')
        self.assertEqual(res.status_code, 404 )




