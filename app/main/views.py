from app.models import Pitch
from flask import render_template
from . import main

#views
@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """

    title='Home-Welcome to One Minute Pitch'


    #categories
    pitches=Pitch.query.all()
    promotion=Pitch.query.filter_by(category='Promotion').all()
    interview=Pitch.query.filter_by(category='Events').all()
    games=Pitch.query.filter_by(category='Games').all()
    product=Pitch.query.filter_by(category='Product').all()

    return render_template('index.html', title=title, pitches=pitches, interview=interview,product=product, promotion=promotion, games=games )


@main.route('/pitches')
def pitches():
    pitches=Pitch.query.all()

    return render_template('pitch.html',pitches=pitches)