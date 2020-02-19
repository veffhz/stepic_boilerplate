class Config:
    APP_PORT = 5000


class ProdConfig(Config):
    ENV = 'production'
    

class DevConfig(Config):
    ENV = 'develop'
