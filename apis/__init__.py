import os

from flask import Flask,  Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy


from config import Config, app_config
app = Flask(__name__)
app.config.from_object(app_config[os.environ.get('ENVIRON', 'production')])

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

from apis.v2 import v2_blueprint as api_v2
from apis.v2 import api_2
# from apis.v1 import v1_blueprint as api_v1
# from apis.v1 import api_1

app.register_blueprint(api_v2)
# app.register_blueprint(api_v1)


