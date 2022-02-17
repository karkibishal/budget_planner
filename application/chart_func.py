from application import app, db
from datetime import timedelta, date
from calendar import monthrange
from application.models import Income, Categories, Expenses

def weeklyExpense():
    cur_date = date.today()
    monday = cur_date - timedelta(days=cur_date.weekday())
    week_date = monday
    weekly_expense = []

    for i in range(7):
        if i == 0:
            expense_per_day = Expenses.query.filter_by(date=week_date).all()
            expense_per_day_total = Expenses.total_expense(expense_per_day)
            weekly_expense.append(expense_per_day_total)
        else:
            week_date += timedelta(days=1)
            expense_per_day = Expenses.query.filter_by(date=week_date).all()
            expense_per_day_total = Expenses.total_expense(expense_per_day)
            weekly_expense.append(expense_per_day_total)

    return weekly_expense


def categoricalExpense():
    categorical_expense = []
    month = date.today().month
    year = date.today().year
    first_date = date(year, month, 1)
    last_date = date(year, month, monthrange(year, month)[1])
    delta = last_date - first_date

    for j in range(12):
        expense_per_category = 0
        for i in range(delta.days + 1):
            month_date = first_date + timedelta(days=i)
            expense_per_day = Expenses.query.filter_by(date=month_date, categories_id=j+1).all()
            expense_per_day_total = Expenses.total_expense(expense_per_day)
            expense_per_category += expense_per_day_total
        categorical_expense.append(expense_per_category)
    
    total_expense = sum(categorical_expense)
    categorical_expense_percent = [x*100/total_expense for x in categorical_expense]
    return categorical_expense_percent


def monthlyExpense():
    monthly_expense = []
    for j in range(12):
        month = j + 1
        year = date.today().year
        first_date = date(year, month, 1)
        last_date = date(year, month, 27)
        delta = last_date - first_date

        expense_month_total = 0

        for i in range(delta.days + 1):
            month_date = first_date + timedelta(days=i)
            expense_per_day = Expenses.query.filter_by(date=month_date).all()
            expense_per_day_total = Expenses.total_expense(expense_per_day)
            expense_month_total += expense_per_day_total

        monthly_expense.append(expense_month_total)

    return monthly_expense