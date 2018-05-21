import re

from flask import Flask, request
from functools import wraps
import jwt
from validate_email import validate_email

# from apis import app
# from apis.v1.models.user import User
# from apis.v1.models.business import BusinessModel
# from apis.v1.models.blacklist import Blacklist

USER_KEYS = ['user_name', 'email', 'password']
RESET_KEYS = ['current_password', 'new_password']
REVIEW_KEYS = ['title', 'body']
BUSINESS_KEYS = ['business_name','category','location','profile']

def validate_user_payload(new_user):
    """ this funtion validates the user payload """

    for key in USER_KEYS:
        if new_user[key] == '':
            return {'message': '{} Cannot be empty'}.format(key), 400

            if key != 'password':
                if not re.match(r'^\w+$', new_user['user_name']):
                    return {'message': 'Enter a valid Username'}, 400

                is_valid_mail = validate_email(new_user['email'])
                if not is_valid_mail:
                    return {'message': 'Enter a Valid Email Address'}, 400
                if len(new_user[key]) > 50 if key == 'user_name' else 120:
                    return {'message': 'user name is too long'}, 400



def validate_reset_payload(new_user):
    """ this endpoint validates password reset payload """
    for key in RESET_KEYS:
        if new_user[key] == '':
            return {'message': '{} Cannot be empty'}.format(key), 400


def validate_review_payload(new_payload):
    """this method validates the review payload """

    for key in REVIEW_KEYS:
        if new_payload[key] == '':
            return {'message': '{} can\'t be empty'}.format(key), 400
        if len(new_payload[key]) > 50 if key == 'title' else 256:
            return {'message': '{} is too long'}.format(key), 400


def validate_business_payload(new_payload):
    """ this method validate the business payload """

    for key in BUSINESS_KEYS:
        if len(new_payload[key]) > 256 if key == 'profile' else 50:
            return {'message': '{} is too long'}.format(key), 400


def validate_business_update_payload(new_payload, businessId):
    """" this method validates the business update payload """


    if new_payload['business_name'] is None and new_payload['category'] is None and new_payload['location'] is None and new_payload['profile'] is None:
        return {'message': 'Payload should have at least one field'}, 400
    for key in BUSINESS_KEYS:
        if len(new_payload[key]) > 256 if key == 'profile' else 50:
            return {'message': '{} is too long'}.format(key), 400