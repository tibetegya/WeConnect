import datetime
from functools import wraps

from werkzeug.security import generate_password_hash,  check_password_hash, safe_str_cmp
from flask import Flask, request, jsonify
from flask_restplus import Namespace, Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import jwt
import json

from apis import app
from apis import db
from apis.v2.models.user import User
from apis.v2.models.blacklist import Blacklist
from apis.v2.utils.decorators import authenticate
from apis.v2.utils.validators import validate_user_payload, validate_reset_payload
from apis.v2.utils.user_models import api, register_model, login_model, reset_model, register_parser, login_parser, reset_parser


class UserRegister(Resource):
    """ This Class handles the registration of a user """

    @api.expect(register_model)
    def post(self):
        """handles registering a user """


        args = register_parser.parse_args()
        new_user = args
        is_not_valid_input = validate_user_payload(args)

        if is_not_valid_input:
            return is_not_valid_input

        # Check for an already existent username
        db_user_with_same_name = User.query.filter_by(user_name=new_user['user_name'].strip(' ')).first()
        db_user_with_same_email = User.query.filter_by(email=new_user['email']).first()

        if (db_user_with_same_name or db_user_with_same_email) is not None:
            return {'message': 'User Already exists'}, 400

        # Register the User
        user_name = new_user['user_name'].strip(' ')
        email = new_user['email'].strip(' ')
        password = new_user['password']

        user_object = User(user_name, email, password)
        db.session.add(user_object)
        db.session.commit()
        return {'message': 'You Are Registered'}, 201

class UserLogin(Resource):
    """ this class handles the loggong in of a user """

    @api.expect(login_model)
    def post(self):
        """ handles posting login data"""

        args = login_parser.parse_args()
        token = ''
        verified = False
        user_name = args['user_name']
        password = args['password']

        # Check if the user exists
        db_user = User.query.filter_by(user_name=user_name).first()

        if db_user is not None:
            if check_password_hash(db_user.password_hash, password):
                token = jwt.encode({
                                    'user': db_user.user_name,
                                    'exp': datetime.datetime.utcnow()
                                        + datetime.timedelta(minutes=100)},
                                    app.config['SECRET_KEY'])
                verified = True
            else:
                return {'message': 'Incorrect password'}, 403

        if verified:
            return {'token': token.decode('UTF-8')}, 200
        else:
            return {'message': 'user does not exist'}, 403


class UserLogout(Resource):
    """ this Class handles the logging out of a user """

    @api.header('Authorization', type=str, description ='Authentication token')
    @authenticate
    def post(self, current_user,token):
        """logs out a user by black listing their access token """

        # token = request.headers.get('Authorization').split(' ')[1]

        token_black_listed = Blacklist(token)
        db.session.add(token_black_listed)
        db.session.commit()

        return {'message': 'you are logged out'}, 200


class UserResetPassword(Resource):
    """ this Class handles resetting of the users password """

    @api.header('Authorization', type=str, description ='Authentication token')
    @api.expect(reset_model)
    def post(self):
        """resets user's password """

        args = reset_parser.parse_args()
        is_not_valid_input = validate_reset_payload(args)

        if is_not_valid_input:
            return is_not_valid_input

        password_payload = args

        db_user = User.query.filter_by(email=args['email'].strip(' ')).first()

        if db_user is not None:

            db_user.password_hash = generate_password_hash(password_payload['new_password'])
            db.session.commit()
            return {'message': 'password is reset'}, 201
        else:
            return {'message': 'email is not valid'}, 400


"""Users Endpoints"""
api.add_resource(UserRegister, '/register', endpoint="Register")
api.add_resource(UserLogin, '/login', endpoint="Login")
api.add_resource(UserLogout, '/logout', endpoint="Logout" )
api.add_resource(UserResetPassword, '/reset-password', endpoint="Reset-password")
