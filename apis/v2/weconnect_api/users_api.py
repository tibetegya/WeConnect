from flask import Flask, request, jsonify
import datetime 
from flask_restplus import Api, Resource, reqparse, fields, marshal_with
from werkzeug.security import generate_password_hash,  check_password_hash, safe_str_cmp
import jwt
import json
import datetime
from functools import wraps  
from flask_sqlalchemy import SQLAlchemy

# local imports
from apis import app
from apis import db
from apis import api
from apis.v2.models.user import User
from apis.v2.models.blacklist import Blacklist
from apis.v2.utils import authenticate, validate_user_payload, is_already_logged_in, validate_reset_payload





'''                                     
=========================================  USERS API  =========================================
                                       
'''


user_model = api.model('user',{'user_name': fields.String('User Name.'),
                                'email': fields.String('Email Address'),
                                'password': fields.String('Password') })

user_login_model = api.model('user_login',{
                                'user_name': fields.String('Username'),
                                'password': fields.String('Password')
                                })
 
password_reset_model = api.model('password_reset',{
                                'current_password': fields.String('Password'),
                                'new_password': fields.String('New Password')  
                                })

class UserRegister(Resource):

    
    @api.expect(user_model)
    def post(self):

        new_user = api.payload 
        is_not_valid_input = validate_user_payload(api.payload)
        if is_not_valid_input:
            return is_not_valid_input
        
        # Check for an already existent username
        db_user_with_same_name = User.query.filter_by(user_name=new_user['user_name']).first()
        db_user_with_same_email = User.query.filter_by(email=new_user['email']).first()

        if (db_user_with_same_name or db_user_with_same_email) != None:
            return {'message': 'User Already exists'} , 403

        # Register the User

        user_name = new_user['user_name'].strip()
        email = new_user['email'].strip()
        password = new_user['password']

        user_object = User(user_name, email, password)
        db.session.add(user_object)
        db.session.commit()
        return {'result':'You Are Registered'}, 201


class UserLogin(Resource):
    @is_already_logged_in
    @api.expect(user_login_model)
    def post(self):
        
        
        token = ''
        verified = False

        user_name = api.payload['user_name']
        password = api.payload['password']
        
        # Check if the user exists
        db_user = User.query.filter_by(user_name=user_name).first()
        if db_user != None: 
            if check_password_hash(db_user.password_hash, password) :
                token = jwt.encode({
                                        'user': db_user.user_name,
                                        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=100)},
                                        app.config['SECRET_KEY'])
                verified = True
        
        if verified:       
            return {'token' : token.decode('UTF-8')}, 200
        else:
            return {'message' : 'user does not exist'}, 403

        


class UserLogout(Resource):

    @authenticate
    def post(self, current_user):
        token = request.headers.get('Authorization').split(' ')[1]
        
        token_black_listed = Blacklist(token)
        db.session.add(token_black_listed)
        db.session.commit()

        return {'result': 'you are logged out'} , 200
        

class UserResetPassword(Resource):
    
    @authenticate
    @api.expect(password_reset_model)
    def post(self, current_user):
        
        is_not_valid_input = validate_reset_payload(api.payload)
        if is_not_valid_input:
            return is_not_valid_input
        password_payload = api.payload
        found = False

        db_user = User.query.filter_by(user_name=current_user).first()
        if db_user != None:
            if check_password_hash(db_user.password_hash, password_payload['current_password']) :
                db_user.password_hash = generate_password_hash(password_payload['new_password'])
                db.session.commit()
                found = True
        
        if found:
            return {'message': 'password is reset'}, 201
        else:
            return {'message': 'user not found You cannot reset password'}, 404

            


     
