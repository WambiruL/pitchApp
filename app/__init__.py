from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

bootstrap=Bootstrap()
db=SQLAlchemy()

#initializing application
app=Flask(__name__)


# Setting up configuration
app.config.from_object(DevConfig)

#initializing extensions
bootstrap.init_app(app)
db.init_app(app)




from app import views