import os


class Config:
    APP_PORT = 5000
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ['FLASK_DB_URL']
    SECRET_KEY = ''


class ProdConfig(Config):
    ENV = 'production'


class DevConfig(Config):
    ENV = 'develop'
    SECRET_KEY = 'some-secret-key'


class TestConfig(Config):
    pass
