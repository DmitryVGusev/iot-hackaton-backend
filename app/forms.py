from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign In')

class Order(FlaskForm):
    client = StringField("Заказчик")
    product = StringField("Изделие")
    count = StringField("Количество")
    date = StringField("Желаемый срок")
    price = StringField("Цена")
    priority = SelectField("Приориет",
                           choices=[(1, 'Высокий'),
                                    (2, 'Общий'),
                                    (3, 'Низкий')],
                           default=2)
    submit = SubmitField('Подтвердить')
