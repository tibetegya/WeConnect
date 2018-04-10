from flask import Flask, Blueprint
from flask_restplus import Resource, Api, fields


# local imports
# from apis import app
#from apis.db import db

# api_v2 = Blueprint('api', __name__)
# api = Api(api_v2, version='2', title= 'WeConnect Api', description= 'WeConnect provides a platform that brings businesses \
#                                                                         \n and individuals together \
#                                                                         And creates awareness for businesses through user reviews')

# ns = api.namespace('v2', description='WeConnect endpoints')

# from apis.v2 import models, weconnect_api, tests