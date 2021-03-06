from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
#from flask_uploads import UploadSet,configure_uploads,IMAGES
import os

bootstrap=Bootstrap()
db=SQLAlchemy()
mail=Mail()

login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

#images=UploadSet('images', IMAGES)
#initializing application
def create_app(config_name):
    app=Flask(__name__)
    

# Setting up configuration
    app.config.from_object(config_options[config_name])
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
  #  app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()
   # app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URI')

#initializing extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    
     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

     # configure UploadSet
    #configure_uploads(app,images)
    

    return app



