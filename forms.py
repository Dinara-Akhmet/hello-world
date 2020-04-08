from wtform import form

from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('��� ������������', validators=[DataRequired()])
    password = PasswordField('������', validators=[DataRequired()])
    remember_me = BooleanField('��������� ����', default=True)
    submit = SubmitField('���������')