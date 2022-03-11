from datetime import date
from application import db

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, nullable = False)
    date = db.Column(db.Date, nullable = False, default = date.today)
    items = db.relationship('Expenses', backref = 'category')

class Expenses(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    amount = db.Column(db.Float, nullable = False)
    date = db.Column(db.Date, nullable = False, default = date.today)
    categories_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable = False)

    def total_expense(expense_list):
        total = 0
        for expense in expense_list:
            total += expense.amount
        return total

class Income(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    salary = db.Column(db.Float, nullable = False, default = 0.0)
    tax = db.Column(db.Float, nullable = False, default = 0.0)
    ni = db.Column(db.Float, nullable = False, default = 0.0)
    pension = db.Column(db.Float, nullable = False, default = 0.0)
    student_loan = db.Column(db.Float, nullable = False, default = 0.0)
    take_home_pay = db.Column(db.Float, nullable = False, default = salary)
    date = db.Column(db.Date, nullable = False, default = date.today)


if __name__ == '__main__':
    db.create_all()