# Insert csv data to db
import csv
from app import app,db
from app.models import Song, User, Artist, Song_Artist, Match

def insert_song(song_path):
    with open(song_path, 'r', encoding = 'utf-8') as file:
        app.app_context().push()
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Create a new Song instance for each row in the csv file
            song = Song(
                id = row['song_id'],
                name = row['track_name'],
                artists = row['artist(s)_name'],
                streams = row['streams'],
                bmp = row['bpm'],
                key = row['key'],
                danceability = row['danceability_%'],
                valence = row['valence_%'],
                energy = row['energy_%'],
                acousticness = row['acousticness_%'],
                instrumentalness = row['instrumentalness_%'],
                liveness = row['liveness_%'],
                speechiness = row['speechiness_%'],
                released_date = row['released_date'],
                promotion = row['promotion']
            )
            db.session.add(song)
        db.session.commit()

def insert_user(user_path):
    with open(user_path, 'r', encoding = 'utf-8') as file:
        app.app_context().push()
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Create a new User instance for each row in the csv file
            user = User(
                id = row['user_id'],
                username = row['user_id'],
                plan = row['plan'],
                password_hash = row['password'],
                age = row['Age'],
                gender = row['Gender'],
                usage_period = row['usage_period'],
                listening_scenario = row['listening_scenario'],
                fav_music_genre = row['fav_music_genre'],
                mood = row['music_Influencial_mood']
            )
            user.set_password('000000')
            db.session.add(user)
        db.session.commit()

def insert_artist(artist_path):
    with open(artist_path, 'r', encoding = 'utf-8') as file:
        app.app_context().push()
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            artist = Artist(
                id = row['artist_id'],
                name = row['artist_name']
            )
            db.session.add(artist)
        db.session.commit()

def insert_song_artist(song_artist_path):
    with open(song_artist_path, 'r', encoding = 'utf-8') as file:
        app.app_context().push()
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            song_artist = Song_Artist(
                song_id = row['song_id'],
                artist_id = row['artist_id']
            )
            db.session.add(song_artist)
        db.session.commit()

def insert_matchability(matchability_path):
    with open(matchability_path, 'r', encoding = 'utf-8') as file:
        app.app_context().push()
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            matchability = Match(
                user_id = row['user_id'],
                song_1 = row['song_1'],
                song_2 = row['song_2'],
                song_3 = row['song_3'],
                song_4 = row['song_4'],
                song_5 = row['song_5']
            )
            db.session.add(matchability)
        db.session.commit()

def set_password_user():
    app.app_context().push()
    users = User.query.all()
    for user in users:
        user.set_password('000000')
       # db.session.add(matchability)
        #assert user.check_password('000000'), "User password not correct"
    