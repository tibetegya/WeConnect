from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from app import app, api
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

users = {
    'user1':{
        'id': 1,
        'user_name': 'tibetegyaGeorge',
        'password': 'tibetegya',
        'email_address': 'tibetegya@andela.com',
        'user_avatar': 'pic.png',
        'business_owned': ['business1', 'business2']
        }, 
    'user2':{
        'id': 2,
        'user_name': 'soniaKarungi',
        'password': 'sonia',
        'email_address': 'SoniaKarungi@andela.com',
        'user_avatar': 'pic.png',
        'business_owned': ['business1', 'business2']
        }, 
    'user3':{
        'id': 3,
        'user_name': 'BrianVan',
        'password': 'Van',
        'email_address': 'BrianVan@andela.com',
        'user_avatar': 'pic.png',
        'business_owned': ['business1', 'business2']
        }, 
    'user4':{
        'id': 4,
        'user_name': 'AtamaZack',
        'password': 'Zack',
        'email_address': 'Zack@andela.com',
        'user_avatar': 'pic.png',
        'business_owned': ['business1', 'business2']
        }       
}


parser = reqparse.RequestParser()
parser.add_argument('user')

class User(Resource):
    def get(self, user_id):
        return users[user_id]
            
    def delete(self, user_id):
        del users[user_id]
        return '', 204

    def put(self, user_id):
        args = parser.parse_args()
        user = {
                    'id': args['id'],
                    'user_name': args['user_name'],
                    'password': args['password'],
                    'email_address': args['email_address'],
                    'user_avatar': args['user_avatar']
                    }
        users[user_id] = user
        return user, 201

class UserList(Resource):
    def get(self):
        return users

    def post(self):
        args = parser.parse_args()
        user_id = int(max(users.keys()).lstrip('user')) + 1
        user_id = 'user%i' % user_id
        users[user_id] = {
                    'id': args['id'],
                    'user_name': args['user_name'],
                    'password': args['password'],
                    'email_address': args['email_address'],
                    'user_avatar': args['user_avatar']
                    }
        return users[user_id], 201
  
api.add_resource(User, '/api/v1/users/<user_id>',)
api.add_resource(UserList, '/api/auth/register' , '/api/v1/users')




