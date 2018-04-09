import os
from flask import Flask  
from config import Config, app_config
from apis.db import db
from apis.v2 import api_v2
from flask_script import Manager
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(app_config['development'])
app.register_blueprint(api_v2, url_prefix='/api')



db.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)



if __name__ == '__main__':
    app.run(debug=True)
    


