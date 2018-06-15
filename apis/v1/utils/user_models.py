from flask_restplus import Namespace, Api, Resource, reqparse, fields

api = Namespace('auth', description='Authorisation operations')


register_model = api.model('user', {'user_name': fields.String('User Name.'),
                                'email': fields.String('Email Address'),
                                'password': fields.String('Password')})

login_model = api.model('user_login', {
                                'user_name': fields.String('Username'),
                                'password': fields.String('Password')
                                })

reset_model = api.model('password_reset', {
                                'current_password': fields.String('Password'),
                                'new_password': fields.String('New Password')
                                })

register_parser = reqparse.RequestParser()

register_parser.add_argument('user_name', required=True, help='user name should be a string', location='json')
register_parser.add_argument('email', required=True, help='email should be a string', location='json')
register_parser.add_argument('password', required=True, help='password should be a string', location='json')

login_parser = register_parser.copy()
login_parser.remove_argument('email')

reset_parser = reqparse.RequestParser()
reset_parser.add_argument('current_password', required=True, help='current password is required', location='json')
reset_parser.add_argument('new_password', required=True, help='new password is required', location='json')