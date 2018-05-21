import re

from flask import Flask, request
from functools import wraps
import jwt
from validate_email import validate_email

from apis import app
from apis.v2.models.user import User
from apis.v2.models.business import BusinessModel
from apis.v2.models.blacklist import Blacklist

SEARCH_KEYS = ['location', 'category']

def validate_user_payload(new_user):
    """ this funtion validates the user payload """

    if new_user['user_name'] == '':
        return {'message': 'Username Cannot be empty'}, 400

    # Check for empty email
    elif new_user['email'] == '':
        return {'message': 'Email Cannot be empty'}, 400

    # Check for empty password
    elif new_user['password'] == '':
        return {'message': 'Password Cannot be empty'}, 400

    # Check for a valid user name
    if not re.match(r'^\w+$', new_user['user_name']):
        return {'message': 'Enter a valid Username'}, 400

    # Check for a valid email
    is_valid_mail = validate_email(new_user['email'])
    if not is_valid_mail:
        return {'message': 'Enter a Valid Email Address'}, 400

    # Check for large/long inputs
    if len(new_user['user_name']) > 50:
        return {'message': 'user name is too long'}, 400

    elif len(new_user['email']) > 120:
        return {'message': 'email is too long'}, 400




def validate_reset_payload(new_user):
    """ this endpoint validates password reset payload """

    # Check for empty current password
    if new_user['current_password'] == '':
        return {'message': 'Old Password Cannot be empty'}, 400

    # Check for empty current password
    elif new_user['new_password'] == '':
        return {'message': 'New Password Cannot be empty'}, 400


def validate_review_payload(new_payload):
    """this method validates the review payload """

    if new_payload['title'] == '':
            return {'message': 'title can\'t be empty'}, 400

    if new_payload['body'] == '':
            return {'message': 'body can\'t be empty'}, 400

    if len(new_payload['title']) > 50:
            return {'message': 'title is too long'}, 400

    elif len(new_payload['body']) > 256:
            return {'message': 'body is too long'}, 400


def validate_business_payload(new_payload):
    """ this method validate the business payload """


    if len(new_payload['business_name']) > 50:
            return {'message': 'name is too long'}, 400

    if len(new_payload['category']) > 50:
            return {'message': 'body is too long'}, 400

    if len(new_payload['location']) > 50:
            return {'message': 'location is too long'}, 400

    if len(new_payload['profile']) > 256:
            return {'message': 'profile is too long'}, 400


def validate_business_update_payload(new_payload, businessId):
    """" this method validates the business update payload """

    if new_payload['business_name'] is None and new_payload['category'] is None and new_payload['location'] is None and new_payload['profile'] is None:
        return {'message': 'Payload should have at least one field'}, 400

    elif len(new_payload['business_name']) > 50:
        return {'message': 'name is too long'}, 400

    elif len(new_payload['category']) > 50:
        return {'message': 'body is too long'}, 400

    elif len(new_payload['location']) > 50:
        return {'message': 'location is too long'}, 400

    elif len(new_payload['profile']) > 256:
        return {'message': 'profile is too long'}, 400

def validate_search_payload(new_payload):
    """" this method validates the business update payload """

    for key in SEARCH_KEYS:
        if new_payload[key] == '':
            return {'message': '{} is too long'.format(key)}, 400
        if new_payload[key] is not None:
            if not re.match(r'^[\w\s]+$', new_payload[key]):
                return {'message': 'Enter valid search arguments'}, 400
