import unittest
from datetime import datetime
from api_v3.weconnect_api import Business

class WeConnectAPITestCase(unittest.TestCase):

    def setUp(self):
        self.my_business = Business()
        self.test_business = {'business_name':'airtel',
                            'id':1,
                            'category': 'tech',
                            'profile': 'pic',
                            'creation_date': datetime.now,
                            'business_owner':'george' }
        self.businesses = { "businesses": []}

    def test_get(self):
        pass
        # self.assertEqual(self.my_business.get(), 
        # self.businesses["businesses"].append(self.test_business))

    
