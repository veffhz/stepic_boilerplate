import os


class Config:
    APP_PORT = 5000


class ProdConfig(Config):
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.environ['FLASK_DB_URL']


class DevConfig(Config):
    ENV = 'develop'
    SQLALCHEMY_DATABASE_URI = os.environ['FLASK_DB_URL']
