from flask import Flask, Blueprint
from flask_restplus import Resource, Api, fields



blueprint = Blueprint('api', __name__)
api = Api(blueprint, version='1', title= 'WeConnect Api', description= 'WeConnect provides a platform that brings businesses \
                                                                        \n and individuals together \
                                                                        And creates awareness for businesses through user reviews')

from v1 import weconnect_api, tests
