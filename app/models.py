from datetime import datetime

from sqlalchemy.orm import backref
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Pitch(db.Model):
    __tablename__='pitch'

    id=db.Column(db.Integer,primary_key=True)
    pitch_title=db.Column(db.String)
    pitch_content=db.Column(db.String(2000))
    category=db.Column(db.String)
    posted=db.Column(db.DateTime, default=datetime.utcnow)
    user_id=db.Column(db.String)
    comment=db.relationship('Comment', backref='pitch', lazy='dynamic')
    upvote = db.relationship('Upvote',backref='pitch',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='pitch',lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

        
    def __repr__(self):
        return f'Pitch {self.pitch_content}'
        
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    email=db.Column(db.String(255), unique=True, index=True)
    username = db.Column(db.String(255))
    pass_secure=db.Column(db.String(255))
    password_hash=db.Column(db.String(255))
    bio=db.Column(db.String(255))
    profile_pic_path=db.Column(db.String())
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvote = db.relationship('Upvote',backref='user',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='user',lazy='dynamic')

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

class Comment(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id=db.Column(db.Integer,db.ForeignKey('pitch.id'))
    comment=db.Column(db.Text())

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):
        comments=Comment.query.filter_by(pitch_id=pitch_id).all()
        return comments

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Comments: {self.comment}'

class Upvote(db.Model):
    __tablename__='upvotes'
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id=db.Column(db.Integer, db.ForeignKey('pitch.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_votes(cls,id):
        upvote=Upvote.query.filter_by(pitch_id=id).all()
        return upvote

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'

class Downvote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_downvotes(cls,id):
        downvote = Downvote.query.filter_by(pitch_id=id).all()
        return downvote

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'

       