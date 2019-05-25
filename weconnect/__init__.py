import os

from flask import Flask
from config import app_config
from weconnect.views.auth import auth_bp
from weconnect.views.business import business_bp

def create_app(testing=False):
  # create and configure the app
  app = Flask(__name__, instance_relative_config=True)
  if testing is False:
    # load the instance config, if it exists, when not testing
    app.config.from_object(app_config[os.environ.get('FLASK_ENV')])
  else:
    # load the test config if passed in
    app.config.from_object(app_config['testing'])
    # app.config.from_mapping(test_config)

  # ensure the instance folder exists
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  # register blueprints
  app.register_blueprint(auth_bp)
  app.register_blueprint(business_bp)

  # a simple page that says hello
  # @app.route('/hello')
  # def hello():
  #   return 'Hello, World!'

  return app
