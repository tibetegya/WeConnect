import os

class Config(object):
  DEBUG = False
  TESTING = False
  DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
  DEBUG = False
  DATABASE_URI = os.environ.get('DATABASE_URI')

class DevelopmentConfig(Config):
  DEBUG = True
  DATABASE_URI = os.environ.get('DATABASE_URI')

class TestingConfig(Config):
  TESTING = True
  DATABASE_URI = os.environ.get('TEST_DATABASE_URI')

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}