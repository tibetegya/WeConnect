import unittest
import flask 
import json
from apis import app
from apis import  api
from apis.v2.tests import ApiTestCase

class BusinessListTestCase(ApiTestCase):
    """ Tests For the Businesses Endpoints """

    def test_get(self):
        res = self.client().get(self.base_url+self.business_list_endpoint)
        
        self.assertEqual(res.status_code, 200 )


    
    # with app.test_request_context():
    #     def test_post(self):
    #         res = self.client().post(self.base_url+self.business_list_endpoint, 
    #                     data=json.dumps(self.test_business),
    #                     content_type='application/json')
    #         #data = json.loads(res.get_data())
            
    #         self.assertEqual(res.status_code, 201 )

#     with app.test_request_context():
#         def test_business_added_name_on_post(self):
#             res = self.client().post(self.base_url+self.business_list_endpoint, 
#                         data=json.dumps(self.test_business),
#                         content_type='application/json')
#             data = json.loads(res.get_data())
#             self.assertEqual(data['business_name']  , 'airtel')

#         def test_delete(self):
#             pass



class BusinessTestCase(ApiTestCase):
    """ Tests For the Single Business Methods and Endpoints  """


    def test_get_(self):
        """ Test For that businesses are retrieved  """

        res = self.client().get(self.base_url+self.business_endpoint)
        self.assertEqual(res.status_code, 404 )



    # def test_put(self):
    #     """ Test For the Single Business has been added  """


    #     res = self.client().put(self.base_url+self.business_endpoint, 
    #                     data=json.dumps(self.test_business),
    #                     content_type='application/json')
    #     self.assertEqual(res.status_code, 201)


#     def test_put_bad_request(self):
#         """ Test For the Single Businessid that is out of range  """


#         res = self.client().put(self.base_url+ self.fake_business_endpoint, 
#                         data=json.dumps(self.test_business),
#                         content_type='application/json')
#         self.assertEqual(res.status_code, 400)



    
   
