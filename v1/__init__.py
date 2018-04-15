from flask import Flask, Blueprint
from config import Config
from flask_restplus import Resource, Api, fields


app = Flask(__name__)

app.config.from_object(Config)
app.config['SWAGGER_UI_JSONEDITOR']= True
app.config['SECRET_KEY'] = 'george is awesome'





api_v1 = Blueprint('api', __name__)
api = Api(api_v1, version='1', title= 'WeConnect Api', description= 'WeConnect provides a platform that brings businesses \
                                                                        \n and individuals together \
                                                                       And creates awareness for businesses through user reviews')

app.register_blueprint(api_v1, url_prefix='/api/v1')

from v1 import weconnect_api, tests
