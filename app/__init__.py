from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy

bootstrap=Bootstrap()
db=SQLAlchemy()

#initializing application
def create_app(config_name):
    app=Flask(__name__)


# Setting up configuration
    app.config.from_object(config_options[config_name])

#initializing extensions
    bootstrap.init_app(app)
    db.init_app(app)




from app import views