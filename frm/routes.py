from frm import app
from flask import Flask, redirect, render_template, request, url_for
from frm.models import db
from frm.models import Movies
from frm.forms import MovieForm

@app.route('/')
@app.route('/home')
def home():
    movieList = Movies.query.all()
    return render_template('mainContent.html', movieList=movieList)

@app.route('/addmovie', methods=['POST', 'GET'])
def addmovie():
    form = MovieForm()
    if form.validate_on_submit():
        print('Submit Works Fine Here')
        print(form.title.data)
        newMovie = Movies(title=form.title.data, description=form.description.data, customer=form.customer.data, category=form.category.data)
        db.session.add(newMovie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('moviefrm.html', form=form, title='Add New Movie')
