import unittest
from weconnect_api import Business, BusinessList, UserAPI, LoginAPI, Review

    
class WeConnectApiTestCase(unittest.TestCase):

    def setUp(self):
        self.my_reviews = Review()
        self.my_user_api = UserAPI()
        self.my_login_api = LoginAPI()
        self.my_business_list = BusinessList()
        self.my_business = Business()


        self.result = [{
        'id': 2,
        'title': 'why i like it here it ',
        'body': 'this is the place to any day',
        'business': 4,
        'author': 'Grace',
        'creation_date': '21 Febuary 2018'        
        }]

        
        self.biz = {
        'id': 2,
        'name': 'Business 2',
        'location': 'mukono',
        'category': 'category2',
        'profile': 'picture.png',
        'creation_date': '21 Febuary 2018',
        'business_owner': 'george'        
        }
        
    
    def test_review_find_reviews(self):
        self.assertEqual(self.my_reviews.find_reviews(4),self.result, msg='Failed To find Reviews')
    
    def test_review_get(self):
            self.assertEqual(type(self.my_reviews.get(4)),dict, msg='revus is not a dictionary')
    
    def test_user_api_post(self):
        self.assertEqual(type(self.my_user_api.post()), list )

    def test_login_api_post(self):
        self.assertEqual(type(self.my_login_api.post()), dict )

    def test_businesslist_post(self):
        self.assertEqual(type(self.my_business_list.post()), dict ) 

    def test_business_put(self):
        self.assertEqual(self.my_business.put('business2'),  self.biz)  

    def test_business_get(self):
        self.assertEqual(self.my_business.get(self.biz), self.biz ) 

    def test_business_delete(self):
        self.assertEqual(self.my_business.delete(self.biz), '' )     




# class UserAPITestCase(unittest.TestCase):

#     def setUp(self):
#         self.my_user_api = UserAPI()
        
#     def test_post(self):
#         self.assertEqual(type(self.my_user_api.post()), list )




# class LoginAPITestCase(unittest.TestCase):


#     def setUp(self):
#         self.my_login_api = LoginAPI()

#     def test_post(self):
#         self.assertEqual(type(self.my_login_api.post()), dict )  






# class BusinessListTestCase(unittest.TestCase):

#     def setUp(self):
#         self.my_business_list = BusinessList()

#     def test_post(self):
#         self.assertEqual(type(self.my_business_list.post()), dict )  






# class BusinessTestCase(unittest.TestCase):

#     def setUp(self):
#         self.my_business = Business()
#         self.biz = {
#         'id': 2,
#         'name': 'Business 2',
#         'location': 'mukono',
#         'category': 'category2',
#         'profile': 'picture.png',
#         'creation_date': '21 Febuary 2018',
#         'business_owner': 'george'        
#         }

#     def test_put(self):
#         self.assertEqual(self.my_business.put('business2'),  self.biz)  

#     def test_get(self):
#         self.assertEqual(self.my_business.get("self.biz"), self.biz ) 

#     def test_delete(self):
#         self.assertEqual(self.my_business.delete('self.biz'), '' )   
