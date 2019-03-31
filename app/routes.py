from app import app
from flask import render_template


@app.route('/')
@app.route('/hello')
def hello():
    return render_template('hello.html')


def login():
    pass