from datetime import datetime
from enum import unique
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class Pitch(db.Model):
    __tablename__='pitch'

    id=db.Column(db.Integer,primary_key=True)
    pitch_title=db.Column(db.String)
    pitch_content=db.Column(db.String(2000))
    category=db.Column(db.String)
    posted=db.Column(db.DateTime, default=datetime.utcnow)
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

        
    def __repr__(self):
        return f'Pitch {self.post}'
        
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    email=db.Column(db.String(255), unique=True, index=True)
    username = db.Column(db.String(255))
    pass_secure=db.Column(db.String(255))
    password_hash=db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'
       