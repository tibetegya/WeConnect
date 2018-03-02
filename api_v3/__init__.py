"""
    :api_v3:
    ~~~~~

    A module for the WeConnect Back End Api using flask-restplus.

    :copyright: (c) 2018 by George Tibetegya.
    :license: MIT, see LICENSE for more details.
"""

from flask import Flask, Blueprint  
from config import Config
from flask_restplus import Resource, Api, fields
from werkzeug.security import generate_password_hash,  check_password_hash



app = Flask(__name__)
app.config.from_object(Config)
blueprint = Blueprint('api', __name__, url_prefix='/api/v3')
api = Api(blueprint, version='3', title= 'WeConnect Api', description= 'WeConnect provides a platform that brings businesses \
                                                                        \n and individuals together \
                                                                        And creates awareness for businesses through user reviews')
app.register_blueprint(blueprint)

# app.config['SWAGGER_UI_JSONEDITOR']= True
app.config['SECRET_KEY'] = 'george is awesome'




        





from api_v3 import weconnect_api, tests
