import unittest
import flask 
import json
from datetime import datetime
from api_v3 import api, app
from api_v3.weconnect_api import Business, Review, businesses, reviews

class ApiTestCase(unittest.TestCase):
    
    def setUp(self):
        self.api =api
        self.app =app
        self.app.testing = True
        self.client = self.app.test_client
        self.businesses = businesses
        self.my_business = Business()
        self.test_business = {'business_name':'airtel',
                            'id':1,
                            'category': 'tech',
                            'profile': 'pic',
                            'creation_date': datetime.now,
                            'business_owner':'george' }
        self.my_list = []

        self.reviews = reviews
        self.my_review = Review()
        self.test_review = {'title':'airtel',
                            'id':1,
                            'body': 'tech',
                            'business': 'airtel',
                            'creation_date': datetime.now,
                            'author':'george' }
        
        


        
        



class BusinessTestCase(ApiTestCase):
    """ Tests For the Business Endpoints """

    def test_get(self):
        res = self.client().get('/api/v3/businesses')
        self.assertEqual(res.status_code, self.my_business.get()[1] )


    
    # with app.test_request_context():
    #     def test_post(self):
    #         res=self.client().post('/api/v3/businesses', 
    #                     data=json.dumps(dict(foo='bar')),
    #                     content_type='application/json')
    #         self.assertEqual(res.status_code, self.my_business.post()[1] )



    
    def test_add_business(self):
        self.assertEqual(self.my_business.add_business(self.test_business), 
                        businesses,
                        msg='business has not been added')




# class ReviewTestCase(ApiTestCase):
#     """ Tests For the Business Endpoints """

#     def test_get(self):
#         biz_id = 0
#         res = self.client().get('/businesses/1/reviews')
#         self.assertEqual(res.status_code, self.my_review.get(biz_id)[1] )



