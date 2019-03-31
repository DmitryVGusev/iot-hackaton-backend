from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import *
import random

variants = [
    [['ibm-300', '1%', '5000%', '|||'], ['ibm-400', '2%', '60%', '|']],
    [['ibmsdfasdf-300', '1%', '5000%', '|||'], ['isadfsdbm-400', '2%', '60%', '|']]
            ]

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' or form.validate_on_submit():
        if form.username.data == 'manager':
            return redirect(url_for('manager'))
        if form.username.data == 'engineer':
            return redirect(url_for('engineer'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/engineer')
def engineer():

    data = variants.pop(0)
    #data = random.choice(variants)
    return render_template('engineer.html', data=data)

@app.route('/manager')
def manager():
    return render_template('manager.html')