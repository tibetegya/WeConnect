import os
from flask import Flask  
from flask_sqlalchemy import SQLAlchemy
from config import Config
from v2 import v2_blueprint as api_v2


app = Flask(__name__)
db = SQLAlchemy()
db.init_app(app)

app.register_blueprint(api_v2, url_prefix='/api/v2')


if __name__ == '__main__':
    app.run(debug=True)
    


