
from extensions import db

class Student(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(30))
    math = db.Column(db.Float())
    english = db.Column(db.Float())
    chemistry = db.Column(db.Float())
    physics = db.Column(db.Float())
    total_mark = db.Column(db.Float())
    