from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_case = db.Column(db.String, unique=True, nullable=False)
    applicant = db.Column(db.String, nullable=False)
    type_applicant = db.Column(db.Integer, nullable=False)
    appraiser = db.Column(db.String, nullable=False)
    judge = db.Column(db.String, nullable=False)
    status_case = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Дело №{}>".format(self.number_case)
