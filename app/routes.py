from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import *
import random
import datetime
import time

"""variants = [
    [['ibm-300', '1%', '5000%', '|||'], ['ibm-400', '2%', '60%', '|']],
    [['ibmsdfasdf-300', '1%', '5000%', '|||'], ['isadfsdbm-400', '2%', '60%', '|']]
            ]"""

def predict_date(count):
    """Высчитываем дату дедлайна"""
    now = datetime.date.today()
    k = random.randint(75, 85) / 100
    v = 600 * k
    predict = round(int(count) / v)
    return now + datetime.timedelta(predict)


    # скорость 5д/ч * ст = 25 д/час = 600 д/сут
    # предикт =  скорость / кол-во деталей /24

variants2 = [
    [
    ['ibm-100', '86%', '52%', '|||'],
    ['ibm-300', '70%', '70%', '||'],
    ['ibm-200', '11%', '59%', '|'],
    ['ibm-400', '10%', '65%', '|'],
    ['ibm-500', '3%', '61%', '|'],
],

    [
        ['ibm-100', '87%', '52%', '|||'],
        ['ibm-300', '71%', '70%', '||'],
        ['ibm-200', '14%', '59%', '|'],
        ['ibm-400', '11%', '65%', '|'],
        ['ibm-500', '4%', '61%', '|'],
    ],
    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '74%', '70%', '||'],
        ['ibm-200', '10%', '59%', '|'],
        ['ibm-400', '7%', '65%', '|'],
        ['ibm-500', '5%', '61%', '|'],
    ],

    [
        ['ibm-100', '85%', '52%', '|||'],
        ['ibm-300', '73%', '70%', '||'],
        ['ibm-200', '11%', '59%', '|'],
        ['ibm-400', '11%', '65%', '|'],
        ['ibm-500', '6%', '61%', '|'],
    ],
    [
        ['ibm-100', '84%', '52%', '|||'],
        ['ibm-300', '74%', '70%', '||'],
        ['ibm-200', '13%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '7%', '61%', '|'],
    ],

    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '72%', '70%', '||'],
        ['ibm-200', '12%', '59%', '|'],
        ['ibm-400', '8%', '65%', '|'],
        ['ibm-500', '6%', '61%', '|'],
    ],
    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '70%', '70%', '||'],
        ['ibm-200', '14%', '59%', '|'],
        ['ibm-400', '7%', '65%', '|'],
        ['ibm-500', '8%', '61%', '|'],
    ],

    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '71%', '70%', '||'],
        ['ibm-200', '13%', '59%', '|'],
        ['ibm-400', '8%', '65%', '|'],
        ['ibm-500', '6%', '61%', '|'],
    ],
    [
        ['ibm-100', '84%', '52%', '|||'],
        ['ibm-300', '74%', '70%', '||'],
        ['ibm-200', '14%', '59%', '|'],
        ['ibm-400', '11%', '65%', '|'],
        ['ibm-500', '7%', '61%', '|'],
    ],

    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '74%', '70%', '||'],
        ['ibm-200', '11%', '59%', '|'],
        ['ibm-400', '10%', '65%', '|'],
        ['ibm-500', '4%', '61%', '|'],
    ],
    [
        ['ibm-100', '87%', '52%', '|||'],
        ['ibm-300', '73%', '70%', '||'],
        ['ibm-200', '11%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '3%', '61%', '|'],
    ],

    [
        ['ibm-100', '84%', '52%', '|||'],
        ['ibm-300', '73%', '70%', '||'],
        ['ibm-200', '10%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '4%', '61%', '|'],
    ],
    [
        ['ibm-100', '85%', '52%', '|||'],
        ['ibm-300', '70%', '70%', '||'],
        ['ibm-200', '12%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '7%', '61%', '|'],
    ],

    [
        ['ibm-100', '87%', '52%', '|||'],
        ['ibm-300', '72%', '70%', '||'],
        ['ibm-200', '12%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '5%', '61%', '|'],
    ],
    [
        ['ibm-100', '86%', '52%', '|||'],
        ['ibm-300', '73%', '70%', '||'],
        ['ibm-200', '10%', '59%', '|'],
        ['ibm-400', '8%', '65%', '|'],
        ['ibm-500', '4%', '61%', '|'],
    ],

    [
        ['ibm-100', '85%', '52%', '|||'],
        ['ibm-300', '71%', '70%', '||'],
        ['ibm-200', '12%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '5%', '61%', '|'],
    ],
    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '72%', '70%', '||'],
        ['ibm-200', '11%', '59%', '|'],
        ['ibm-400', '7%', '65%', '|'],
        ['ibm-500', '7%', '61%', '|'],
    ],

    [
        ['ibm-100', '84%', '52%', '|||'],
        ['ibm-300', '74%', '70%', '||'],
        ['ibm-200', '13%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '5%', '61%', '|'],
    ],
    [
        ['ibm-100', '86%', '52%', '|||'],
        ['ibm-300', '73%', '70%', '||'],
        ['ibm-200', '10%', '59%', '|'],
        ['ibm-400', '7%', '65%', '|'],
        ['ibm-500', '6%', '61%', '|'],
    ],

    [
        ['ibm-100', '87%', '52%', '|||'],
        ['ibm-300', '71%', '70%', '||'],
        ['ibm-200', '14%', '59%', '|'],
        ['ibm-400', '8%', '65%', '|'],
        ['ibm-500', '4%', '61%', '|'],
    ]
]
variants = [
    [
        ['ibm-100', '25%', '52%', '|'],
        ['ibm-200', '14%', '59%', '|'],
        ['ibm-300', '12%', '70%', '|'],
        ['ibm-400', '10%', '65%', '|'],
        ['ibm-500', '8%', '61%', '|'],
    ],
    [
        ['ibm-100', '26%', '52%', '|'],
        ['ibm-200', '15%', '59%', '|'],
        ['ibm-300', '14%', '70%', '|'],
        ['ibm-400', '11%', '65%', '|'],
        ['ibm-500', '7%', '61%', '|'],
    ],
    [
        ['ibm-300', '73%', '70%', '||'],
        ['ibm-100', '26%', '52%', '|'],
        ['ibm-200', '15%', '59%', '|'],
        ['ibm-400', '11%', '65%', '|'],
        ['ibm-500', '7%', '61%', '|'],
    ],
    [
        ['ibm-100', '85%', '52%', '|||'],
        ['ibm-300', '72%', '70%', '||'],
        ['ibm-200', '12%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '5%', '61%', '|'],
    ],
    [
        ['ibm-100', '86%', '52%', '|||'],
        ['ibm-300', '70%', '70%', '||'],
        ['ibm-200', '11%', '59%', '|'],
        ['ibm-400', '10%', '65%', '|'],
        ['ibm-500', '3%', '61%', '|'],
    ],

    [
        ['ibm-100', '87%', '52%', '|||'],
        ['ibm-300', '71%', '70%', '||'],
        ['ibm-200', '14%', '59%', '|'],
        ['ibm-400', '11%', '65%', '|'],
        ['ibm-500', '4%', '61%', '|'],
    ],
    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '74%', '70%', '||'],
        ['ibm-200', '10%', '59%', '|'],
        ['ibm-400', '7%', '65%', '|'],
        ['ibm-500', '5%', '61%', '|'],
    ],

    [
        ['ibm-100', '85%', '52%', '|||'],
        ['ibm-300', '73%', '70%', '||'],
        ['ibm-200', '11%', '59%', '|'],
        ['ibm-400', '11%', '65%', '|'],
        ['ibm-500', '6%', '61%', '|'],
    ],
    [
        ['ibm-100', '84%', '52%', '|||'],
        ['ibm-300', '74%', '70%', '||'],
        ['ibm-200', '13%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '7%', '61%', '|'],
    ],

    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '72%', '70%', '||'],
        ['ibm-200', '12%', '59%', '|'],
        ['ibm-400', '8%', '65%', '|'],
        ['ibm-500', '6%', '61%', '|'],
    ],
    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '70%', '70%', '||'],
        ['ibm-200', '14%', '59%', '|'],
        ['ibm-400', '7%', '65%', '|'],
        ['ibm-500', '8%', '61%', '|'],
    ],

    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '71%', '70%', '||'],
        ['ibm-200', '13%', '59%', '|'],
        ['ibm-400', '8%', '65%', '|'],
        ['ibm-500', '6%', '61%', '|'],
    ],
    [
        ['ibm-100', '84%', '52%', '|||'],
        ['ibm-300', '74%', '70%', '||'],
        ['ibm-200', '14%', '59%', '|'],
        ['ibm-400', '11%', '65%', '|'],
        ['ibm-500', '7%', '61%', '|'],
    ],

    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '74%', '70%', '||'],
        ['ibm-200', '11%', '59%', '|'],
        ['ibm-400', '10%', '65%', '|'],
        ['ibm-500', '4%', '61%', '|'],
    ],
    [
        ['ibm-100', '87%', '52%', '|||'],
        ['ibm-300', '73%', '70%', '||'],
        ['ibm-200', '11%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '3%', '61%', '|'],
    ],

    [
        ['ibm-100', '84%', '52%', '|||'],
        ['ibm-300', '73%', '70%', '||'],
        ['ibm-200', '10%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '4%', '61%', '|'],
    ],
    [
        ['ibm-100', '85%', '52%', '|||'],
        ['ibm-300', '70%', '70%', '||'],
        ['ibm-200', '12%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '7%', '61%', '|'],
    ],

    [
        ['ibm-100', '87%', '52%', '|||'],
        ['ibm-300', '72%', '70%', '||'],
        ['ibm-200', '12%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '5%', '61%', '|'],
    ],
    [
        ['ibm-100', '86%', '52%', '|||'],
        ['ibm-300', '73%', '70%', '||'],
        ['ibm-200', '10%', '59%', '|'],
        ['ibm-400', '8%', '65%', '|'],
        ['ibm-500', '4%', '61%', '|'],
    ],

    [
        ['ibm-100', '85%', '52%', '|||'],
        ['ibm-300', '71%', '70%', '||'],
        ['ibm-200', '12%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '5%', '61%', '|'],
    ],
    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '72%', '70%', '||'],
        ['ibm-200', '11%', '59%', '|'],
        ['ibm-400', '7%', '65%', '|'],
        ['ibm-500', '7%', '61%', '|'],
    ],

    [
        ['ibm-100', '84%', '52%', '|||'],
        ['ibm-300', '74%', '70%', '||'],
        ['ibm-200', '13%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '5%', '61%', '|'],
    ],
    [
        ['ibm-100', '86%', '52%', '|||'],
        ['ibm-300', '73%', '70%', '||'],
        ['ibm-200', '10%', '59%', '|'],
        ['ibm-400', '7%', '65%', '|'],
        ['ibm-500', '6%', '61%', '|'],
    ],

    [
        ['ibm-100', '87%', '52%', '|||'],
        ['ibm-300', '71%', '70%', '||'],
        ['ibm-200', '14%', '59%', '|'],
        ['ibm-400', '8%', '65%', '|'],
        ['ibm-500', '4%', '61%', '|'],
    ],
    [
        ['ibm-100', '86%', '52%', '|||'],
        ['ibm-300', '70%', '70%', '||'],
        ['ibm-200', '11%', '59%', '|'],
        ['ibm-400', '10%', '65%', '|'],
        ['ibm-500', '3%', '61%', '|'],
    ],

    [
        ['ibm-100', '87%', '52%', '|||'],
        ['ibm-300', '71%', '70%', '||'],
        ['ibm-200', '14%', '59%', '|'],
        ['ibm-400', '11%', '65%', '|'],
        ['ibm-500', '4%', '61%', '|'],
    ],
    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '74%', '70%', '||'],
        ['ibm-200', '10%', '59%', '|'],
        ['ibm-400', '7%', '65%', '|'],
        ['ibm-500', '5%', '61%', '|'],
    ],

    [
        ['ibm-100', '85%', '52%', '|||'],
        ['ibm-300', '73%', '70%', '||'],
        ['ibm-200', '11%', '59%', '|'],
        ['ibm-400', '11%', '65%', '|'],
        ['ibm-500', '6%', '61%', '|'],
    ],
    [
        ['ibm-100', '84%', '52%', '|||'],
        ['ibm-300', '74%', '70%', '||'],
        ['ibm-200', '13%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '7%', '61%', '|'],
    ],

    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '72%', '70%', '||'],
        ['ibm-200', '12%', '59%', '|'],
        ['ibm-400', '8%', '65%', '|'],
        ['ibm-500', '6%', '61%', '|'],
    ],
    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '70%', '70%', '||'],
        ['ibm-200', '14%', '59%', '|'],
        ['ibm-400', '7%', '65%', '|'],
        ['ibm-500', '8%', '61%', '|'],
    ],

    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '71%', '70%', '||'],
        ['ibm-200', '13%', '59%', '|'],
        ['ibm-400', '8%', '65%', '|'],
        ['ibm-500', '6%', '61%', '|'],
    ],
    [
        ['ibm-100', '84%', '52%', '|||'],
        ['ibm-300', '74%', '70%', '||'],
        ['ibm-200', '14%', '59%', '|'],
        ['ibm-400', '11%', '65%', '|'],
        ['ibm-500', '7%', '61%', '|'],
    ],

    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '74%', '70%', '||'],
        ['ibm-200', '11%', '59%', '|'],
        ['ibm-400', '10%', '65%', '|'],
        ['ibm-500', '4%', '61%', '|'],
    ],
    [
        ['ibm-100', '87%', '52%', '|||'],
        ['ibm-300', '73%', '70%', '||'],
        ['ibm-200', '11%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '3%', '61%', '|'],
    ],

    [
        ['ibm-100', '84%', '52%', '|||'],
        ['ibm-300', '73%', '70%', '||'],
        ['ibm-200', '10%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '4%', '61%', '|'],
    ],
    [
        ['ibm-100', '85%', '52%', '|||'],
        ['ibm-300', '70%', '70%', '||'],
        ['ibm-200', '12%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '7%', '61%', '|'],
    ],

    [
        ['ibm-100', '87%', '52%', '|||'],
        ['ibm-300', '72%', '70%', '||'],
        ['ibm-200', '12%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '5%', '61%', '|'],
    ],
    [
        ['ibm-100', '86%', '52%', '|||'],
        ['ibm-300', '73%', '70%', '||'],
        ['ibm-200', '10%', '59%', '|'],
        ['ibm-400', '8%', '65%', '|'],
        ['ibm-500', '4%', '61%', '|'],
    ],

    [
        ['ibm-100', '85%', '52%', '|||'],
        ['ibm-300', '71%', '70%', '||'],
        ['ibm-200', '12%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '5%', '61%', '|'],
    ],
    [
        ['ibm-100', '83%', '52%', '|||'],
        ['ibm-300', '72%', '70%', '||'],
        ['ibm-200', '11%', '59%', '|'],
        ['ibm-400', '7%', '65%', '|'],
        ['ibm-500', '7%', '61%', '|'],
    ],

    [
        ['ibm-100', '84%', '52%', '|||'],
        ['ibm-300', '74%', '70%', '||'],
        ['ibm-200', '13%', '59%', '|'],
        ['ibm-400', '9%', '65%', '|'],
        ['ibm-500', '5%', '61%', '|'],
    ],
    [
        ['ibm-100', '86%', '52%', '|||'],
        ['ibm-300', '73%', '70%', '||'],
        ['ibm-200', '10%', '59%', '|'],
        ['ibm-400', '7%', '65%', '|'],
        ['ibm-500', '6%', '61%', '|'],
    ],

    [
        ['ibm-100', '87%', '52%', '|||'],
        ['ibm-300', '71%', '70%', '||'],
        ['ibm-200', '14%', '59%', '|'],
        ['ibm-400', '8%', '65%', '|'],
        ['ibm-500', '4%', '61%', '|'],
    ]

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


@app.route('/manager', methods=['GET', 'POST'])
def manager():
    form = Order()
    if request.method == 'POST' or form.validate_on_submit():
        plan_date = datetime.datetime.strptime(form.date.data, '%d.%m.%Y')
        # now.strftime("%d.%m.%Y")
        pred_count = predict_date(form.count.data)
        unix_predict = time.mktime(pred_count.timetuple())
        unix_date = time.mktime(plan_date.date().timetuple())
        #return "{} {}".format(unix_date, unix_predict)

        if unix_date > unix_predict:
            deadline = True
        else:
            deadline = False

        answer = [form.client.data,
                  form.product.data,
                  form.count.data,
                  form.price.data,
                  form.priority.data,
                  form.date.data,
                  pred_count.strftime('%d.%m.%Y'),
                  deadline]
        return render_template('manager-2.html', form=answer)

    return render_template('manager.html', form=form)