import os 

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://lorraine:1234@localhost/apppitch'
   # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
  #  UPLOADED_PHOTOS_DEST ='app/static/images'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
   # SQLALCHEMY_DATABASE_URI ='sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI= 'postgresql://nryiboddqrgrqm:0b5247f70271b5ac51e536049b85e13f46977bd985ae7fdfe49f27bd09c6b201@ec2-35-174-35-242.compute-1.amazonaws.com:5432/ddatno0d7s23g6'

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}