from getpass import getpass  # аналог input(), только скрытыми символами
import sys

from webapp import create_app
from webapp.model import db, User


app = create_app()  # создаем app локально, для работы с б/д

with app.app_context():  # открывает доступ для работы с б/д
    username = input('Введите имя пользователя:')

    if User.query.filter(User.username == username).count():
        print('Такой пользователь уже существует')
        sys.exit(0)

    roles = ('admin', 'user', 'guest')
    role = input('Введите роль пользователя (admin, user, guest):')
    if role not in roles:
        print('Роль пользователя введена не верно.')
        sys.exit(0)

    password1 = getpass('Введите пароль:')
    password2 = getpass('Введите повторно пароль:')
    if not password1 == password2:
        print("Пароли не одинаковые")
        sys.exit(0)

    new_user = User(username=username, role=role)
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print('Добавлен пользователь {}'.format(new_user.username))
