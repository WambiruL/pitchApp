from flask import Flask
from flask_bootstrap import Bootstrap
#initializing application
app=Flask(__name__)

#initializing extensions
bootstrap=Bootstrap(app)

from app import views