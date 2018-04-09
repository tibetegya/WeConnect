from flask import Flask, Blueprint
from flask_restplus import Resource, Api, fields


# local imports
from run import app
from apis.db import db

db.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)


api_v2 = Blueprint('api', __name__)
api = Api(api_v2, version='2', title= 'WeConnect Api', description= 'WeConnect provides a platform that brings businesses \
                                                                        \n and individuals together \
                                                                        And creates awareness for businesses through user reviews')

from apis.v2 import models, weconnect_api, tests