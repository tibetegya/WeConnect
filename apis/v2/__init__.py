from flask import Flask, Blueprint
from flask_restplus import Resource, Api, fields
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

blueprint = Blueprint('api', __name__)
api = Api(blueprint, version='2', title= 'WeConnect Api', description= 'WeConnect provides a platform that brings businesses \
                                                                        \n and individuals together \
                                                                        And creates awareness for businesses through user reviews')

from apis.v2 import models, weconnect_api, tests