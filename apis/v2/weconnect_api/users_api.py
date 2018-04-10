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
from apis import ns as api
from apis.v2.models.user import User
from apis.v2.models.blacklist import Blacklist





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
            
            token_blacklisted = Blacklist.query.filter_by(token=token).first()

            if token_blacklisted:
                return {'message' : 'Token is expired!'}, 401 
            try: 
                print('try is working')
                data = jwt.decode(token, app.config['SECRET_KEY'])
                user = data['user']
                current_user = user
                print(str(user))
                if user:
                    print('if starts off as working')
                    request.data = json.loads(request.data) if len(request.data) else {}
                    request.data['current_user'] = current_user 
                    print('if is working')
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
        user_name = new_user['user_name']
        email = new_user['email']
        password = new_user['password']

        # Check for empty username
        if new_user['user_name'].strip() == '':
            return {'message': 'Username Cannot be empty'} , 403

        # Check for empty email
        elif new_user['email'].strip() == '':
            return {'message': 'Email Cannot be empty'} , 403

        # Check for empty password
        elif new_user['password'].strip() == '':
            return {'message': 'Password Cannot be empty'} , 403
        
        
        # Check for an already existent username
        db_user = User.query.filter_by(user_name=new_user['user_name']).first()
        
        if db_user != None:
            return {'message': 'User Already exists'} , 403

        # Register the User
        user_object = User(user_name, email, password)
        db.session.add(user_object)
        db.session.commit()
        return {'result':'You Are Registered'}, 201


class UserLogin(Resource):
    
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
                                        'user': db_user,
                                        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10)},
                                        app.config['SECRET_KEY'])
                verified = True
        
        if verified:       
            return {'token' : token.decode('UTF-8')}, 200
        else:
            return {'message' : 'user does not exist'}, 404

        


class UserLogout(Resource):

    @authenticate
    def post(self):
        token = request.headers.get('Authorization').split(' ')[1]
        
        token_black_listed = Blacklist(token)
        db.session.add(token_black_listed)
        db.session.commit()

        return {'result': 'you are logged out'} , 200
        

class UserResetPassword(Resource):
    
    @authenticate
    @api.expect(password_reset_model)
    def post(self):

        current_user = request.data['current_user']
        password_payload = api.payload
        found = False

        db_user = User.query.filter_by(user_name=current_user).first()
        if db_user != None:
            if check_password_hash(db_user.password_hash, password_payload['current_password']) :
                db_user.password_hash = generate_password_hash(password_payload['new_password'])
                db.session.add(db_user.password_hash)
                db.session.commit()
                found = True
        
        if found:
            return {'message': 'password is reset'}, 201
        else:
            return {'message': 'user not found You cannot reset password'}, 404

            


     
