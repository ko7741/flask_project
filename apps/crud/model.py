from datetime import datetime

from apps.app import db


class Chat(db.Model):

    __tablename__="chat"

    id = db.Column(db.Integer, primary_key=True)
    friendname = db.Column(db.String)
    friend_chating = db.Column(db.String)
    my_chatting = db.Column(db.String)
    chatting_time=db.Column(db.DateTime, default= datetime.now)
    chatting_update_time=db.Column(db.DateTime, default= datetime.now, onupdate=datetime.now)

    def __repr__(self):
         return '<Post: %r>' % (self.title)