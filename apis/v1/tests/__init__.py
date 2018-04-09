import unittest
import flask 
import json
from datetime import datetime
from app import app
from v1 import api
from ..weconnect_api import Business, BusinessList, Review, businesses, reviews

class ApiTestCase(unittest.TestCase):
    
    def setUp(self):
        self.api =api
        self.app =app
        self.app.testing = True
        self.client = self.app.test_client
        self.base_url = '/api/v1'

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
        
