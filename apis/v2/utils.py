from flask import Flask, request, jsonify
from functools import wraps
import jwt
import re
from validate_email import validate_email

# local imports
from apis import app
from apis.v2.models.user import User
from apis.v2.models.business import BusinessModel
from apis.v2.models.blacklist import Blacklist

def authenticate (f):
    @wraps(f)    
    def decorated(*args, **kwargs):
        token_auth_header = request.headers.get('Authorization')
        current_user = ''
        if token_auth_header:

            token = token_auth_header.split(' ')[1]
            if not token:
                return {'message' : 'Token is missing!'}, 401 
            
            token_blacklisted = Blacklist.query.filter_by(token=token).first()

            if token_blacklisted:
                return {'message' : 'Token is expired!'}, 401 
            try: 
                data = jwt.decode(token, app.config['SECRET_KEY'])
                matched_user = User.query.filter_by(user_name=data['user']).first()
                current_user = matched_user.user_name

            except jwt.exceptions.InvalidTokenError:
                return {'message' : 'Token is invalid!'} , 401
        else:
            return {'message' : 'unauthorised'}, 401
        return f(*args, current_user, **kwargs)
    return decorated


def validate_user_payload (new_user):

        # Check for non existent fields
        if not ('user_name' in new_user.keys() and 'email' in new_user.keys() and 'password' in new_user.keys()):
            return {'message': 'Payload should not have missing fields'} , 403
        # Check for empty username
        if new_user['user_name'].strip() == '':
            return {'message': 'Username Cannot be empty'} , 403
        # Check for empty email
        elif new_user['email'].strip() == '':
            return {'message': 'Email Cannot be empty'} , 403
        # Check for empty password
        elif new_user['password'].strip() == '':
            return {'message': 'Password Cannot be empty'} , 403

        # Check for a valid user name
        if not re.match('^\w+$', new_user['user_name']):
            return {'message': 'Enter a valid Username'} , 403

        # Check for a valid email
        is_valid_mail = validate_email(new_user['email'])
        if not is_valid_mail:
            return {'message': 'Enter a Valid Email Address'} , 403

        #check for large/long inputs 
        if len(new_user['user_name']) > 50:
            return {'message': 'user name is too long'} , 400
        elif len(new_user['email']) > 120:
            return {'message': 'email is too long'} , 400

def is_already_logged_in (f):
    @wraps(f)    
    def decorated(*args, **kwargs):
        token_auth_header = request.headers.get('Authorization')
        current_user = ''
        if token_auth_header:

            token = token_auth_header.split(' ')[1]
            
            token_blacklisted = Blacklist.query.filter_by(token=token).first()

            if token_blacklisted == None:
                return {'message' : 'You are Already logged in '}, 200 
            
        return f(*args, **kwargs)
    return decorated

def validate_reset_payload (new_user):
    # Check for non existent fields
        if not ('current_password' in new_user.keys() and 'new_password' in new_user.keys()):
            return {'message': 'Payload should not have missing fields'} , 403
        # Check for empty current password
        elif new_user['current_password'].strip() == '':
            return {'message': 'Old Password Cannot be empty'} , 403
        # Check for empty current password
        elif new_user['new_password'].strip() == '':
            return {'message': 'New Password Cannot be empty'} , 403

