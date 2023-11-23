from flask import render_template, flash, redirect,url_for
from app import app
from app.forms import LoginForm, MusicSearchForm
from flask_login import current_user, login_user
#from app.models import User
from flask_login import logout_user
from flask_login import login_required
from flask import request,flash, render_template, redirect
from werkzeug.urls import url_parse
#from db_setup import init_db, db_session
from app.models import User, Artist, Song, Match
#from tables import Results
from sqlalchemy import func



@app.route('/')
@app.route('/index', methods=['GET','POST'])
@login_required
def index():
    if current_user.id:
        match = Match.query.filter_by(user_id = current_user.id)[0]
        song_ids = [match.song_1,match.song_2,match.song_3,match.song_4,match.song_5]
        songs = Song.query.filter(Song.id.in_(song_ids)).all()
    else:
        songs = Song.query.all()[:5]
    global search #
    search = MusicSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
 
    return render_template('index.html', form=search,  songs = songs)
    #return render_template("index.html", title='Home Page', posts=posts)

@app.route('/results', methods=['GET','POST'])
def search_results():
    search = MusicSearchForm(request.form)

    search_string = search.data['search']
 
    if search_string:
        search_string = search_string.lower()
        if search.data['select'] == 'Artist':
            qry = Artist.query.filter(func.lower(Artist.name).contains(search_string))#(func.lower(Artist.name).contains(search_string) )
            results = qry.all()
            if not results:
                flash('No results found!')
                return redirect(url_for('index'))
            return render_template('results_artist.html', artists = results)
        else:
            qry = Song.query.filter(func.lower(Song.name).contains(search_string))
            results = qry.all()
            if not results:
                flash('No results found!')
                return redirect(url_for('index'))
            return render_template('results_song.html', songs = results)
    elif not search_string:
        flash('No results found!')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))