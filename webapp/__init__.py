from flask import Flask, render_template, request
from flask_login import LoginManager

from webapp.model import db, Case
from webapp.user.models import User
from webapp.admin.views import blueprint as admin_blueprint
from webapp.user.views import blueprint as user_blueprint


def create_app():  # "фабрика" - функция которая создает Flask app, инициализирует его и возвращает app
    app = Flask(__name__)
    app.config.from_pyfile('config.py')  # считывает конфигурацию с файла config.py
    db.init_app(app)  # инициализация б/д

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'  # функция login будет заниматся логином пользователя
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(user_blueprint)

    # проверяем пользователя
    @login_manager.user_loader  # login_manager вытаскивает из сессионой cookie user_id
    def load_user(user_id):  # пeредает user_id и load_user
        return User.query.get(user_id)  # запрашиваем из б/д

    @app.route('/')
    def index():  # -> html
        return render_template('entry.html')

    @app.route('/write_db/', methods=['POST'])
    def write_case_db():  # -> html
        number_case = request.form['number_case']
        applicant = request.form['applicant']
        type_applicant = request.form['type_applicant']
        appraiser = request.form['appraiser']
        judge = request.form['judge']
        status_case = request.form['status_case']
        case_exist = Case.query.filter(Case.number_case == number_case).count()
        print(case_exist)
        if not case_exist:
            new_case = Case(number_case=number_case, applicant=applicant,
                            type_applicant=type_applicant, appraiser=appraiser,
                            judge=judge, status_case=status_case)
            db.session.add(new_case)
            db.session.commit()
            field_titles = ('ID', 'Номер дела', 'Заявитель', 'Тип заявителя',
                            'Оценщик', 'Судья', 'Статус дела')
            case_list = Case.query.all()
            print(case_list)
            return render_template('results.html', field_titles=field_titles,
                                   case_list=case_list)
        return render_template('results_error.html', the_number=number_case)

    return app
