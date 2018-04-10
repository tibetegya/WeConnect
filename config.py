import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:andela123@localhost/weconnectdb')
    
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True



class TestingConfig(Config):
    TESTING = True
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:andela123@localhost/test_weconnectdb"




class ProductionConfig(Config):
    DEBUG = False
    
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
