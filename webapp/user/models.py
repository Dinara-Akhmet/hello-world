from flask_login import UserMixin  # содержит в себе методы is_authenticated,
# is_anonymous, is_anonymous
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.model import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    password = db.Column(db.String(32), nullable=False)
    nick = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    middle_name = db.Column(db.String(64))
    role = db.Column(db.String(64), nullable=False, index=True)
    superuser = db.Column(db.String(64))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return "<Пользователь: {}, ID: {}>".format(self.username, self.id)
