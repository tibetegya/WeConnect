import os
from flask import Flask  
from flask_sqlalchemy import SQLAlchemy

from config import Config
from v1 import blueprint as api_v1
from v2 import v2_blueprint as api_v2


app = Flask(__name__)
db = SQLAlchemy()



app.config.from_object(Config)
app.config['SWAGGER_UI_JSONEDITOR']= True
app.config['SECRET_KEY'] = 'george is awesome'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(api_v1, url_prefix='/api/v1')
app.register_blueprint(api_v2, url_prefix='/api/v2')


if __name__ == '__main__':
    app.run(debug=True)
    


