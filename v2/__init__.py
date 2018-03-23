from flask import Flask, Blueprint
from flask_restplus import Resource, Api, fields



v2_blueprint = Blueprint('v2_api', __name__)
v2_api = Api(v2_blueprint, version='2', title= 'WeConnect Api', description= 'WeConnect provides a platform that brings businesses \
                                                                        \n and individuals together \
                                                                        And creates awareness for businesses through user reviews')

#from v2 import models, tests
