from flask import Flask, request
from config import Config
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()



from app import weconnect_api
