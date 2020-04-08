from webapp import db, create_app

db.create_all(app=create_app())  # создание всех таблиц в б/д
