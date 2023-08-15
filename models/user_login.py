from extensions import db
from flask_login import UserMixin


class Register(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(30), nullable = False)
    phone_number = db.Column(db.Integer())