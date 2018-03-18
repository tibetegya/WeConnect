"""
    :weconnect_api:
    ~~~~~
    
    A module that contains the endpoints for the WeConnect restful API (flask-restplus).

"""

from flask import Flask, request, jsonify
import datetime 
from flask_restplus import Api, Resource, reqparse, fields, marshal_with
from werkzeug.security import generate_password_hash,  check_password_hash, safe_str_cmp
from werkzeug.datastructures import FileStorage
import jwt
import json
import datetime
from functools import wraps


from v1 import api, app
from .reviews_api import Review, reviews










'''                                     
=========================================  USERS API  =========================================
                                       
'''


user_model = api.model('user',{'user_name': fields.String('User Name.'),
                                'email': fields.String('Email Address'),
                                'password': fields.String('Password'),
                                'profile': fields.String('Profile Photo') })

user_login_model = api.model('user_login',{
                                'user_name': fields.String('Username'),
                                'password': fields.String('Password')
                                })
 
password_reset_model = api.model('password_reset',{
                                'current_password': fields.String('Password'),
                                'new_password': fields.String('New Password')  
                                })

 
# user_parser = reqparse.RequestParser()
# user_parser.add_argument('user_name', type=str, help='Username Must be a string',location='json',required=True)
# user_parser.add_argument('email', type=str, help='Email must be string',location='json',required=True)
# user_parser.add_argument('password', type=str, help='Password Must be a string',location='json',required=True)
# user_parser.add_argument('profile', type=FileStorage, help='photo Must be a string',location='files')


users = []
token_black_list = []

def authenticate (func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token_auth_header = request.headers.get('Authorization')
        if token_auth_header:
            print('checking')
            print(request.headers)
            print('after')
            token = token_auth_header.split(' ')[1]
            if not token:
                return {'message' : 'Token is missing!'}, 401 
            if token in token_black_list:
                return {'message' : 'Token is expired!'}, 401 
            try: 
                print('try is working')
                data = jwt.decode(token, app.config['SECRET_KEY'])
                user = data['user']
                #current_user = user
                print(str(user))
                # if user:
                #     print('if starts off as working')
                #     request.data = json.loads(request.data) if len(request.data) else {}
                #     request.data['current_user'] = current_user 
                #     print('if is working')
            except:
                return {'message' : 'Token is invalid!'} , 401
        else:
            return {'message' : 'unauthorised'}, 401
        return func(*args, **kwargs)
    return decorated



class UserRegister(Resource):

    
    @api.expect(user_model)
    def post(self):

        new_user = api.payload
        if new_user['user_name'].strip() == '':
            return {'message': 'Username Cannot be empty'} , 403
        elif new_user['email'].strip() == '':
            return {'message': 'Email Cannot be empty'} , 403
        elif new_user['password'].strip() == '':
            return {'message': 'Password Cannot be empty'} , 403
        for u in users:
            if new_user['user_name'] == u['user_name']:
                return {'message': 'User Already exists'} , 403

        new_user['id'] = len(users)+1
        # pw_hash = generate_password_hash(new_user['password'])
        # new_user['password'] = pw_hash 
        users.append(new_user)
        return {'result':'You Are Registered'}, 201


class UserLogin(Resource):
    
    @api.expect(user_login_model)
    
    def post(self):
        
        
        token = ''
        verified = False

        user_name = api.payload['user_name']
        password = api.payload['password']
        
        for user in users:
            if user_name == user['user_name'] and password == user['password']:
                token = jwt.encode({
                                    'user': user['user_name'],
                                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10)},
                                    app.config['SECRET_KEY'])
                verified = True

        if verified:       
            return {'token' : token.decode('UTF-8')}, 200
        else:
            return {'message' : 'user not found'}, 404


class UserLogout(Resource):

    @authenticate
    def post(self):
        token = request.headers.get('Authorization').split(' ')[1]
        
        token_black_list.append(token)
        return {'result': 'you are logged out'} , 200
        

class UserResetPassword(Resource):
    
    @authenticate
    @api.expect(password_reset_model)
    def post(self):
        current_user = request.data['current_user']
        password_payload = api.payload
        found = False
        for u in users:
            if current_user == u['user_name'] and password_payload['current_password']==u['password']:
                u['password'] = password_payload['new_password']
                found = True
        if found:
            return {'message': 'password is reset'}, 201
        else:
            return {'message': 'user not found You cannot reset password'}, 404

            


     



        






'''                                     
=========================================  BUSINESSES API  =========================================
                                        
'''

businesses = []



business_model = api.model('business',{'business_name': fields.String('the business name.'),
                # 'id': fields.Integer(1),
                'location': fields.String('the business\'s location.'),
                'category': fields.String('the business category.'),
                'profile': fields.String('the business logo.')
                # 'creation_date': fields.Date(),
                # 'business_owner': fields.String('user that created')
                })

class BusinessList(Resource):

    @api.doc(responses={
        400: 'Validation Error',
        401: 'Bearer Authentication Error'
    }, id ='get_all_businesses' )
    #@api.header('token', type=str, description ='Authentication token')
    #@authenticate
    @api.marshal_with(business_model, code=200 , description='Displays a list of registered Businesses')
    def get(self):
        return businesses , 200


    #@authenticate
    @api.expect(business_model)
    def post(self):
        new_biz = api.payload
        new_biz['id'] = len(businesses)+1
        businesses.append(new_biz)
        return businesses[-1] , 201


class Business(Resource):

    def get(self, businessId):
        return businesses[businessId-1], 200
    
    @api.expect(business_model)
    def put(self, businessId):
        biz_to_change = api.payload
        found = False
        if type(businessId) == int :
            if businessId > len(businesses):
                return {'message': 'bad request Yo !'}, 400
            else:
                for biz in businesses:
                    if biz['id'] == biz_to_change['id']:
                        found = True
                        businesses[businessId-1] = biz_to_change
                        return {'result': 'business changed successfully'}, 201
        if found == False :
            return {'result': 'business does not exist'}, 404

        
    
    def delete(self, businessId ):
        biz_to_delete = api.payload
        if type(businessId) != int :
            return {'message': 'business id must be an integer'}, 400
        else:
            if businessId > len(businesses):
                return {'message': 'bad request Yo!'}, 400
            else:
                for biz in businesses:
                    if biz['id'] ==  biz_to_delete['id']:
                            
                            del businesses[businessId-1]
                            return {'result': 'business deleted'}, 201
                else:
                    return {'message': 'We Don\' t know that business Yo!'}, 404












api.add_resource(Business, '/businesses/<int:businessId>', endpoint="business")
api.add_resource(BusinessList, '/businesses', endpoint="businesses")
api.add_resource(Review, '/businesses/<int:businessId>/reviews', endpoint="reviews")

api.add_resource(UserRegister, '/auth/register', endpoint="Register")
api.add_resource(UserLogin, '/auth/login', endpoint="Login")
api.add_resource(UserLogout, '/auth/logout', endpoint="Logout" )
api.add_resource(UserResetPassword, '/auth/reset-password', endpoint="Reset-password")



