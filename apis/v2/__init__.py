from flask import Flask, Blueprint
from flask_restplus import Resource, Api, fields
from flask_sqlalchemy import SQLAlchemy

# local imports
from run import app

db = SQLAlchemy(app)
db.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)


blueprint = Blueprint('api', __name__)
api = Api(blueprint, version='2', title= 'WeConnect Api', description= 'WeConnect provides a platform that brings businesses \
                                                                        \n and individuals together \
                                                                        And creates awareness for businesses through user reviews')

from apis.v2 import models, weconnect_api, tests