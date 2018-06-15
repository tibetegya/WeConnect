from flask import Blueprint
from flask_restplus import Api

from apis.v2.weconnect_api.users_api import api as ns1
from apis.v2.weconnect_api.business_api import api as ns2
from apis.v2.weconnect_api.reviews_api import api as ns3

v2_blueprint = Blueprint('api_two', __name__, url_prefix='/api/v2')
api_2 = Api(v2_blueprint, version='2.0',
            title= 'WeConnect Api',
            description= 'WeConnect provides a platform that brings businesses \
            \n and individuals together \
            And creates awareness for businesses through user reviews')

api_2.add_namespace(ns1)
api_2.add_namespace(ns2)
api_2.add_namespace(ns3)

