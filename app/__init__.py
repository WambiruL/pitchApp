from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
import os

bootstrap=Bootstrap()
db=SQLAlchemy()

#initializing application
def create_app(config_name):
    app=Flask(__name__)


# Setting up configuration
    app.config.from_object(config_options[config_name])
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY

#initializing extensions
    bootstrap.init_app(app)
    db.init_app(app)

     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app



