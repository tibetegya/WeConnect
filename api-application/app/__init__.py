from flask import Flask, request
from config import Config
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


<<<<<<< HEAD
from app import business_api
=======
from app import user_api

>>>>>>> user-api
