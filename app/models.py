from datetime import datetime
from . import db

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