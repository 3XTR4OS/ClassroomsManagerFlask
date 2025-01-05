from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField
from wtforms import Form
from wtforms import TextAreaField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class LoginForm(Form):
    openid = TextAreaField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class CabSearchForm(FlaskForm):
    cab_is_gym = BooleanField('Спортивный зал', default=False)
    cab_is_small = BooleanField('Малый кабинет', default=False)
    cab_with_projector = BooleanField('Наличие проектора', default=False)
    cab_is_computer = BooleanField('Компьютерный кабинет', default=False)
    submit = SubmitField('Фильтровать')


if __name__ == '__main__':
    cabs = CabSearchForm()
