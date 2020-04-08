import os

basedir = os.path.abspath(os.path.dirname(__file__))
# в переменную basedir сохраняет абсолютный путь к config.py (__file__)

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
# sqlite:///C:\projects\learn_web\webapp\..\webapp.db

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + basedir + '\\..\\' + 'webapp.db'
SECRET_KEY = "asdhphvw2efw523rda"
