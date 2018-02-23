import unittest
from app.review_api import Review
class ReviewTestCase(unittest.TestCase):

    def setUp(self):
        self.my_reviews = Review()
        self.result = [{
        'id': 2,
        'title': 'why i like it here it ',
        'body': 'this is the place to any day',
        'business': 4,
        'author': 'Grace',
        'creation_date': '21 Febuary 2018'        
        }]
    
    def test_find_reviews(self):
        self.assertEqual(self.my_reviews.find_reviews(4),self.result, msg='Failed To find Reviews')
    
    def test_get(self):
            self.assertEqual(type(self.my_reviews.get(4)),dict, msg='revus is not a dictionary')
    


