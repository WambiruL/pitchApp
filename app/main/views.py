from app.main.forms import PitchForm
from app.models import Pitch
from flask import render_template, url_for,redirect
from flask_login import login_required
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

@main.route('/new_pitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
    pitch_form=PitchForm()
    if pitch_form.validate_on_submit():
        title=pitch_form.title.data
        pitch=pitch_form.pitch.data
        category=pitch_form.category.data

        new_pitch=Pitch(pitch_title=title, pitch_content=pitch, category=category)

        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title='New Pitch'

    return render_template('new_pitch.html', title=title, pitch_form=pitch_form)
