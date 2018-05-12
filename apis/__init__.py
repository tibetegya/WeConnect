import os

from flask import Flask,  Blueprint
from flask_restplus import Api  
from flask_script import Manager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config, app_config


# from apis.db import db
api_v2 = Blueprint('api', __name__)
api = Api(api_v2, version='2', title= 'WeConnect Api', description= 'WeConnect provides a platform that brings businesses \
                                                                        \n and individuals together \
                                                                        And creates awareness for businesses through user reviews')

# api_v1 = Blueprint('api', __name__)
# api = Api(api_v1, version='1', title= 'WeConnect Api', description= 'WeConnect provides a platform that brings businesses \
#                                                                         \n and individuals together \
#                                                                         And creates awareness for businesses through user reviews')

# ns = api.namespace('v2', description='WeConnect endpoints')

app = Flask(__name__)
app.config.from_object(app_config['development'])
app.register_blueprint(api_v2, url_prefix='/api/v2')
# app.register_blueprint(api_v2, url_prefix='/api/v1')

db = SQLAlchemy(app)

from apis.v2.models.blacklist import Blacklist
from apis.v2.models.review import ReviewModel
from apis.v2.models.business import BusinessModel
from apis.v2.models.user import User
from apis.v2 import weconnect_api

# db.create_all()
# manager = Manager(app)
