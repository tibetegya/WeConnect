from flask import Blueprint
from flask_restplus import Api


api_v1 = Blueprint('api_one', __name__)
api_1 = Api(api_v1, version='2',
            title= 'WeConnect Api',
            description= 'WeConnect provides a platform that brings businesses \
            \n and individuals together \
            And creates awareness for businesses through user reviews')

ns_1 = api_1.namespace('v1', description='WeConnect endpoints')