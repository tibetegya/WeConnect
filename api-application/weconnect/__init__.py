"""
    :weconnect:
    ~~~~~

    A module for the WeConnect Back End Api.

    :copyright: (c) 2018 by George Tibetegya.
    :license: MIT, see LICENSE for more details.
"""

from flask import Flask, request,render_template, url_for
from config import Config
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)



from weconnect import weconnect_api, tests
