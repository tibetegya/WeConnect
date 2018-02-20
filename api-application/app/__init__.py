from flask import Flask
from flask_api import FlaskAPI

app = Flask(__name__)
app = FlaskAPI(__name__)


from app import routes