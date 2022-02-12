from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Income, Categories, Items
from application.forms import IncomeForm, ItemsForm

@app.route('/', methods=['POST', 'GET'])
def index():
    annual_salary = Income.query.all()
    return render_template('index.html', title="Budget Planner", annual_salary=annual_salary)

@app.route('/categories', methods=['POST', 'GET'])
def categories():
    categories = Categories.query.all()
    return render_template('categories.html', title="Categories", categories=categories)

@app.route('/income', methods=['POST', 'GET'])
def income():
    form = IncomeForm()
    if form.validate_on_submit():
        if form.select_salary.data == "annual":
            salary = form.salary.data
        elif form.select_salary.data == "monthly":
            salary = form.salary.data * 12
        elif form.select_salary.data == "weekly":
            salary = form.salary.data * 52 

        if form.select_tax.data == "annual":
            tax = form.tax.data
        elif form.select_tax.data == "monthly":
            tax = form.tax.data * 12
        elif form.select_tax.data == "weekly":
            tax = form.tax.data * 52

        if form.select_ni.data == "annual":
            ni = form.ni.data
        elif form.select_ni.data == "monthly":
            ni = form.ni.data * 12
        elif form.select_ni.data == "weekly":
            ni = form.ni.data * 52
            
        if form.select_pension.data == "annual":
            pension = form.pension.data
        elif form.select_pension.data == "monthly":
            pension = form.pension.data * 12
        elif form.select_pension.data == "weekly":
            pension = form.pension.data * 52

        if form.select_student_loan.data == "annual":
            student_loan = form.student_loan.data
        elif form.select_student_loan.data == "monthly":
            student_loan = form.student_loan.data * 12
        elif form.select_student_loan.data == "weekly":
            student_loan = form.student_loan.data * 52

        income = Income(
                    salary = salary,
                    tax = tax,
                    ni = ni,
                    pension = pension,
                    student_loan = student_loan
                    )
        db.session.add(income)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('income.html', title="Add income details", form=form)

@app.route('/items', methods=['POST', 'GET'])
def items():
    form = ItemsForm()
    if form.validate_on_submit():
        if form.select.data == "annual":
            amount = form.amount.data / 12
        elif form.select.data == "monthly":
            amount = form.amount.data
        elif form.select.data == "weekly":
            amount = form.amount.data * 4.33

        item = Items(
                    name = form.name.data,
                    amount = amount
                    )
        db.session.add(item)
        db.commit()
        return redirect(url_for('index'))
    return render_template('items.html', title="Add expense items", form=form)