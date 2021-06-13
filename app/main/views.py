from flask import render_template
from . import main

#views
@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """

    title='Home-Welcome to Pitch Your Project'

    #categories

    return render_template('index.html', title=title)

    return render_template