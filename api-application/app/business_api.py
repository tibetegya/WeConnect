from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from app import app, api

businesses = {
    'business1':{
        'id': 1,
        'name': 'Business 1',
        'location': 'kampala',
        'category': 'category2',
        'profile': 'picture.png',
        'creation_date': '21 Febuary 2018',
        'business_owner': 'george'        
        },
    'business2':{
        'id': 2,
        'name': 'Business 2',
        'location': 'mukono',
        'category': 'category2',
        'profile': 'picture.png',
        'creation_date': '21 Febuary 2018',
        'business_owner': 'george'        
        },
}


parser = reqparse.RequestParser()
parser.add_argument('business')

class Business(Resource):
    def get(self, business_id):
        return businesses[business_id]
        
    def delete(self, business_id):
        del businesses[business_id]
        return '', 204
    def put(self, business_id):
        args = parser.parse_args()
        business = {
                    'id': args['id'] ,
                    'name': args['name'],
                    'location': args['location'],
                    'category': args['category'],
                    'profile': args['profile'],
                    'creation_date': args['date'],
                    'business_owner': args['business_owner']        
                    }
        businesses[business_id] = business
        return business, 201

class BusinessList(Resource):
    def get(self):
        return businesses

    def post(self):
        args = parser.parse_args()
        business_id = int(max(businesses.keys()).lstrip('business')) + 1
        business_id = 'business%i' % business_id
        businesses[business_id] = {
                    'id': args['id'] ,
                    'name': args['name'],
                    'location': args['location'],
                    'category': args['category'],
                    'profile': args['profile'],
                    'creation_date': args['date'],
                    'business_owner': args['business_owner']        
                    }
        return businesses[business_id], 201

api.add_resource(BusinessList, '/api/v1/businesses')
api.add_resource(Business, '/api/v1/businesses/<business_id>')
