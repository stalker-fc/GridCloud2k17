"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from FlaskWebProject import app
from FlaskWebProject.random_string import getNewPassword

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    if not hasattr(app, 'background_color'):
        app.background_color = '#FF0000'

    return render_template(
        'index.html',
        background_color=app.background_color,
    )

@app.route('/password/<length>')
def getPassword(length=None):
    return getNewPassword(int(length))

@app.route('/color', methods=['POST'])
def changeColor():
    if not request.is_json:
        return 'FAILED'
    content = request.get_json()
    if content['color'] is None or content['color'] == '':
        app.background_color = '#FAEBD7'
    else:
        app.background_color = content['color']
    print(app.background_color)
    return 'SUCCESS'