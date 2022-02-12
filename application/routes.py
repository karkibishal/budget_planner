from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Income
from application.forms import IncomeForm

@app.route('/', methods=['POST', 'GET'])
def index():
    annual_salary = Income.query.first()
    return render_template('index.html', title="Budget Planner", annual_salary=annual_salary)

@app.route('/income', methods=['POST', 'GET'])
def income():
    form = IncomeForm()
    if form.validate_on_submit():
        if form.selection.data == "annual":
            salary = form.annual_salary.data
        elif form.selection.data == "monthly":
            salary = form.annual_salary.data * 12
        elif form.selection.data == "weekly":
            salary = form.annual_salary.data * 52 
        income = Income(
                    annual_salary = salary,
                    tax = form.tax.data,
                    ni = form.ni.data,
                    pension = form.pension.data,
                    student_loan = form.student_loan.data
                    )
        db.session.add(income)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('income.html', title="Add income details", form=form)
