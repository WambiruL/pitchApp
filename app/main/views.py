from app.main.forms import CommentForm, PitchForm
from app.models import Comment, Pitch, User
from flask import render_template, url_for,redirect,abort
from flask_login import login_required,current_user
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
        return redirect(url_for('.pitches'))

    title='New Pitch'

    return render_template('new_pitch.html', title=title, pitch_form=pitch_form)

@main.route('/comment/<int:pitch_id>', methods=['GET','POST'])
@login_required
def comment(pitch_id):
    form=CommentForm()
    pitch=Pitch.query.get(pitch_id)
    user=User.query.all()
    comments=Comment.query.filter_by(pitch_id=pitch_id).all()
    if form.validate_on_submit():
        comment=form.comment.data
        pitch_id=pitch_id
        user_id=current_user._get_current_object().id
        new_comment= Comment(
            comment=comment,
            pitch_id=pitch_id,
            user_id=user_id
        )

        new_comment.save()
        new_comments=[new_comment]
        print(new_comments)
        return redirect(url_for('.comment', pitch_id=pitch_id))
    return render_template('comments.html', form=form, pitch=pitch, comments=comments,user=user)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

