from datetime import datetime
from application import db

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, nullable = False)
    created_at = db.Column(db.DateTime, nullable = False, default = datetime.now)
    updated_at = db.Column(db.DateTime, nullable = False, default = datetime.now, onupdate = datetime.now)
    items = db.relationship('Expenses', backref = 'category')

class Expenses(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    amount = db.Column(db.Float, nullable = False)
    created_at = db.Column(db.DateTime, nullable = False, default = datetime.now)
    updated_at = db.Column(db.DateTime, nullable = False, default = datetime.now, onupdate = datetime.now)
    categories_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable = False)

class Income(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    salary = db.Column(db.Float, nullable = False)
    tax = db.Column(db.Float, nullable = False)
    ni = db.Column(db.Float, nullable = False)
    pension = db.Column(db.Float, nullable = False)
    student_loan = db.Column(db.Float, nullable = False)
