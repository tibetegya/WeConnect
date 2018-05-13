import os

from flask import Flask,  Blueprint
from flask_sqlalchemy import SQLAlchemy


from config import Config, app_config
app = Flask(__name__)


app.config.from_object(app_config['development'])

db = SQLAlchemy(app)
from apis.v2 import v2_blueprint as api_v2
# from apis.v2 import api_2

app.register_blueprint(api_v2)
# app.register_blueprint(api_1, url_prefix='/api/v1')


