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
from app.models import User, Artist, Song
from tables import Results




@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    songs = Song.query.all()
    search = MusicSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
 
    return render_template('index.html', form=search,  songs = songs)
    #return render_template("index.html", title='Home Page', posts=posts)

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
 
    if search_string:
        if search.data['select'] == 'Artist':
            qry = Artist.query().filter_by(name = search_string)
            results = qry.all()
        else:
            qry = Song.query().filter_by(name = search_string)
            results = qry.all()
 
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)

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