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
    age = db.Column(db.String)
    gender = db.Column(db.String)
    usage_period = db.Column(db.String)
    listening_scenario = db.Column(db.String)
    fav_music_genre = db.Column(db.String)
    mood = db.Column(db.String)

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
    streams = db.Column(db.Integer)
    bmp = db.Column(db.Integer)
    key = db.Column(db.String)
    danceability = db.Column(db.Integer)
    valence = db.Column(db.Integer)
    energy = db.Column(db.Integer)
    acousticness = db.Column(db.Integer)
    instrumentalness = db.Column(db.Integer)
    liveness = db.Column(db.Integer)
    speechiness = db.Column(db.Integer)
    released_date = db.Column(db.DateTime)
    promotion = db.Column(db.Integer)

    #artist = db.relationship("Artist", backref=db.backref("albums", order_by=id), lazy=True)

class Song_Artist(db.Model):

    __tablename__ = "song_artist"

    song_id = db.Column(db.String, primary_key = True)
    artist_id = db.Column(db.String, primary_key = True)

class Match(db.Model):

    __tablename__ = "matchability"

    id = db.Column(db.String, primary_key = True)
    song_1 = db.Column(db.String)
    song_2 = db.Column(db.String)
    song_3 = db.Column(db.String)
    song_4 = db.Column(db.String)
    song_5 = db.Column(db.String)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))