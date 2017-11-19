import json
from flask import Flask
from flask import render_template, request
from random_string import getNewPassword

app = Flask(__name__)


@app.route('/')
def index():
    print(app.background_color)
    return render_template('index.html', background_color=app.background_color)

@app.route('/color', methods=['POST'])
def changeColor():
    if not request.is_json:
        return 'FAILED'
    content = request.get_json()
    if content['color'] is None or content['color'] == '':
        app.background_color = '#FAEBD7'
    else:
        app.background_color = content['color']

    return 'SUCCESS'

@app.route('/password/<length>')
def getPassword(length=None):
    return getNewPassword(int(length))

if __name__ == '__main__':
    app.background_color = "#FAEBD8"
    app.run()
