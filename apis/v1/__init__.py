from flask import Blueprint
from flask_restplus import Api

from apis.v1.weconnect_api.users_api import api as ns1
from apis.v1.weconnect_api.business_api import api as ns2
from apis.v1.weconnect_api.reviews_api import api as ns3
from apis.v1.db import Database

v1_blueprint = Blueprint('api_one', __name__, url_prefix='/api/v1')
api_1 = Api(v1_blueprint, version='1',
            title= 'WeConnect Api',
            description= 'WeConnect provides a platform that brings businesses \
            \n and individuals together \
            And creates awareness for businesses through user reviews')

db = Database()

api_1.add_namespace(ns1)
api_1.add_namespace(ns2)
api_1.add_namespace(ns3)