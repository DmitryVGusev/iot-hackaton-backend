from app import app
from flask import render_template, request
from app.forms import *



@app.route('/')
@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        ans = request
        print(some)
    return render_template('new_login.html', title='Log in', form=form)