"""
    :weconnect_api:
    ~~~~~
    
    A module that contains the endpoints for the WeConnect restful API (flask-restplus).

"""

from flask import Flask, request, jsonify
from datetime import datetime
from flask_restplus import Api, Resource, reqparse, fields, marshal_with
from api_v3 import api
from werkzeug.security import generate_password_hash,  check_password_hash, safe_str_cmp
'''
USERS API

'''


user_model = api.model('user',{'user_name': fields.String('User Name.'),
                                'email': fields.String('Email Address'),
                                'password': fields.String('Password'),
                                'profile': fields.String('Profile Photo') })

user_login_model = api.model('user_login',{
                                'user_name': fields.String('Username'),
                                'password': fields.String('Password')
                                })
 
user_logout_model = api.model('user_logout',{
                                'token': fields.String('Authentication Token') 
                                })

users = []
class UserRegister(Resource):
   
    @api.expect(user_model)
    def post(self):
        new_user = api.payload
        new_user['id'] = len(users)+1
        pw_hash = generate_password_hash(new_user['password'])
        new_user['password'] = pw_hash 
        users.append(new_user)
        return {'result':'You Are Registered'}, 201


class UserLogin(Resource):
    @api.expect(user_login_model)
    def post(self):
        #check if user exists
        user_name = api.payload['user_name']
        password = api.payload['password']
        password_hash = generate_password_hash(password)
        for user in users:
            if user_name == user['user_name'] and password_hash == user['password']:
                pass
        

class UserLogout(Resource):
    @api.expect(user_logout_model)
    def post(self):
        pass

class UserResetPassword(Resource):
 
    def post(self):
        pass


class User(Resource):
 
    def get(self):
        pass

        






'''
BUSINESSES API

'''


business_model = api.model('business',{'business_name': fields.String('the business name.'),'id': fields.Integer(1),
                'location': fields.String('the business\'s location.'),
                'category': fields.String('the business category.'),
                'profile': fields.String('the business logo.'),
                # 'creation_date': fields.Date(),
                'business_owner': fields.String('user that created')})


businesses = []

# business1 = {'busines_name':'business1', 'id': 1, 'location':'kampala','profile':'logo.png',
#             'creation_date':'21 Feb 2018','busines_owner':'george'}
# businesses.append(business1)


class Business(Resource):

    def add_business(self, new_biz):
        new_biz['id'] = len(businesses)+1
        businesses.append(new_biz)
        return businesses


    @api.marshal_with(business_model)
    def get(self):
        return businesses , 200

    @api.expect(business_model)
    def post(self):
        self.add_business(api.payload)
        return {'result':'business Added'}, 201

class BusinessList(Resource):

    def update_business(self, business_to_update):
        pass

    def get(self, businessId):
        return businesses[businessId-1], 200

    @api.expect(business_model)
    def put(self, businessId):
        biz_changed = api.payload
        for biz in businesses:
            if biz['id'] == biz_changed['id']:
                businesses[businessId-1] = biz_changed
                return {'result': 'business changed successfully'}, 201


        return {'result': 'business does not exist'}, 500
    
    def delete(self, businessId ):
        del businesses[businessId-1]
        return {'message': 'business deleted'}, 201

'''
REVIEWS API

'''


review_model = api.model('review',{'title': fields.String('review title.'),
                # 'id': fields.Integer(1),
                'body': fields.String('body'),
                # 'business': fields.Integer(),
                'author': fields.String('user that created'),
                # 'creation_date': fields.Date() 
                 })


reviews = []
class Review(Resource):

    @api.marshal_with(review_model, envelope='reviews')
    def get(self, businessId):
        biz_reviews = []
        for rev in reviews:
            if rev['business'] == businessId:
                biz_reviews.append(rev)

        return biz_reviews

    @api.expect(review_model)
    # @api.marshal_with(review_model, envelope='reviews')
    def post(self, businessId):
        new_review = api.payload
        new_review['id'] = len(reviews)+1
        new_review['business'] = businessId
        new_review['creation_date'] = '%s'%(datetime.now())

        reviews.append(new_review)
        return {'result':'Review Added'}, 201



api.add_resource(BusinessList, '/businesses/<int:businessId>', endpoint="business")
api.add_resource(Business, '/businesses', endpoint="businesses")
api.add_resource(Review, '/businesses/<int:businessId>/reviews', endpoint="reviews")

api.add_resource(UserRegister, '/auth/register', endpoint="Register")
api.add_resource(UserLogin, '/auth/login', endpoint="Login")
api.add_resource(UserLogout, '/auth/logout', endpoint="Logout" )
api.add_resource(UserResetPassword, '/auth/reset-password', endpoint="Reset-password")
api.add_resource(User, '/auth/users', endpoint="users")


