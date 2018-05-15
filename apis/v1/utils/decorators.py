from functools import wraps

from flask import request
import jwt

from apis import app
from apis.v1.models.blacklist import Blacklist
from apis.v1.models.user import User


def authenticate(f):
    """this decorator function handles user authentication"""

    @wraps(f)
    def decorated(*args, **kwargs):

        token_auth_header = request.headers.get('Authorization')
        current_user = ''
        token = ''
        if token_auth_header:
            try:
                token = token_auth_header if not 'Bearer' in token_auth_header else token_auth_header.split(' ')[1]
            except IndexError:
                return {'message': 'Token is missing!'}, 401

            token_blacklisted = Blacklist.query.filter_by(token=token).first()

            if token_blacklisted is not None:
                return {'message': 'Token is expired!'}, 401

            try:
                data = jwt.decode(token, app.config['SECRET_KEY'])
                matched_user = User.query.filter_by(user_name=data['user']).first()
                current_user = matched_user.user_name

            except jwt.exceptions.InvalidTokenError:
                return {'message': 'Token is invalid!'}, 401

        else:
            return {'message': 'unauthorised'}, 401

        return f(*args, current_user, token, **kwargs)

    return decorated
