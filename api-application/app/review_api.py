from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from app import app, api


reviews = [
    {
        'id': 1,
        'title': 'why i like it here it ',
        'body': 'this is the place to any day',
        'business': 1,
        'author': 'George',
        'creation_date': '21 Febuary 2018'
        },
    {
        'id': 2,
        'title': 'why i like it here it ',
        'body': 'this is the place to any day',
        'business': 4,
        'author': 'Grace',
        'creation_date': '21 Febuary 2018'        
        },
    {
        'id': 3,
        'title': 'why i like it here it ',
        'body': 'this is the place to any day',
        'business': 1,
        'author': 'Brian',
        'creation_date': '21 Febuary 2018'
        },
    {
        'id': 4,
        'title': 'why i like it here it ',
        'body': 'this is the place to any day',
        'business': 2,
        'author': 'Richard',
        'creation_date': '21 Febuary 2018'        
        }
]




parser = reqparse.RequestParser()
parser.add_argument('review')

class Review(Resource):

    def find_reviews(self, biz_id):
        business_reviews = []

        for review in reviews:
            if review['business'] == biz_id:
                business_reviews.append(review)
        
        return business_reviews

    def get(self, business_id):
        biz_reviews = self.find_reviews(business_id)
        revus = {}
        for i in range(len(biz_reviews)):
            revus[str(i)] = biz_reviews[i] 

        return revus
    def post(self, business_id):
        args = parser.parse_args()
        rev_dict = {
            'id': args['id'],
            'title': args['title'],
            'body': args['body'],
            'business': args['business'],
            'author': args['author'],
            'creation_date': args['creation_date']
        } 
        reviews.append(rev_dict)
        return reviews[len(reviews)], 201




api.add_resource(Review, '/api/businesses/<int:business_id>/reviews')