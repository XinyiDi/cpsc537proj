from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class User(UserMixin, db.Model):
    id = db.Column(db.String(120), primary_key=True)
    username = db.Column(db.String(120))
    plan = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))


    def __repr__(self):
        return '<User {}>'.format(self.id)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Artist(db.Model):
    __tablename__ = "artists"
 
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
 
    def __repr__(self):
        return "<Artist: {}>".format(self.name)

class Song(db.Model):
    """"""
    __tablename__ = "songs"
 
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    artists = db.Column(db.String)
    #artist = db.relationship("Artist", backref=db.backref("albums", order_by=id), lazy=True)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))