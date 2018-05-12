import datetime
from functools import wraps

from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, reqparse, fields, marshal_with
from werkzeug.security import generate_password_hash,  check_password_hash, safe_str_cmp
from werkzeug.datastructures import FileStorage
import jwt
import json

from apis import app
from apis import api


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

users = []
token_black_list = []


def authenticate (func):
    """ decorator method for jwt token authentication. """

    @wraps(func)
    def decorated(*args, **kwargs):

        token_auth_header = request.headers.get('Authorization')

        if token_auth_header:
            token = token_auth_header.split(' ')[1]

            if not token:
                return {'message' : 'Token is missing!'}, 401
            if token in token_black_list:
                return {'message' : 'Token is expired!'}, 401
            try:
                data = jwt.decode(token, app.config['SECRET_KEY'])
                user = data['user']
                #current_user = user
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
    """ Class that handles the registration of users """


    @api.expect(user_model)
    def post(self):
        """ method for posting user registration data """

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
    """ Class that handles logging in users """


    @api.expect(user_login_model)
    def post(self):
        """ method for logging in a user """

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
    """ Class that handles the logging out of a user """


    @authenticate
    def post(self):
        """ method that handles the logging out of a user """

        token = request.headers.get('Authorization').split(' ')[1]

        token_black_list.append(token)
        return {'result': 'you are logged out'} , 200



class UserResetPassword(Resource):
    """ Class that handles resetting of a user's password """


    @authenticate
    @api.expect(password_reset_model)
    def post(self):
        """ method that handles the password reset endpoint """

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
