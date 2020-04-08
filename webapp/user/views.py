from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from webapp.user.forms import LoginForm
from webapp.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login/')
def login():
    if current_user.is_authenticated:  # если авторизован то перенапрваляет на страницу с index()
        #  is_authenticated - метод, но выглядит как атрибут, без ()
        return redirect(url_for('index'))
    title = 'Авторизация'
    login_form = LoginForm()
    return render_template('login.html', page_title=title, the_form=login_form)


@blueprint.route('/process-login/', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():  # проверка на ошибки, могут возникнуть при вводе данных пользователем в форму
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash("Вы успешно вошли на сайт")
            return redirect(url_for('index'))  # перенаправляет на страницу по названию ф-ции
    flash("Неправильное имя или пароль")
    return redirect(url_for('user.login'))


@blueprint.route('/logout/')
def logout():
    logout_user()
    flash("Вы успешно разлогинились")
    return redirect(url_for('index'))
