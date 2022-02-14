from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Income, Categories, Expenses
from application.forms import IncomeForm, ExpensesForm

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

@app.route('/expenses', methods=['POST', 'GET'])
def expenses():
    return render_template('expenses.html')

@app.route('/add_expense', methods=['POST', 'GET'])
def add_expense():
    form = ExpensesForm()
    if form.validate_on_submit():
        
        expense = Expenses(
                    name = form.name.data,
                    amount = form.amount.data,
                    categories_id = Categories.query.filter_by(name=form.select_cat.data).first().id
                    )
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('add_expense'))
    return render_template('add_expense.html', title="Add expense items", form=form)

@app.route('/view_expenses', methods=['POST', 'GET'])
def view_expenses():
    all_expenses = Expenses.query.order_by(Expenses.updated_at.desc()).all()
    return render_template('view_expenses.html', title="Budget Planner", all_expenses=all_expenses)

@app.route('/edit_expense/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    expense = Expenses.query.get(id)
    form = ExpensesForm(name = expense.name, select_cat = expense.category.name, amount = expense.amount)
    if form.validate_on_submit():
        expense.name = form.name.data
        expense.amount = form.amount.data
        expense.categories_id = Categories.query.filter_by(name=form.select_cat.data).first().id
        db.session.commit()
        return redirect(url_for('view_expenses'))
    elif request.method == 'GET':
        form = form
    return render_template('edit_expense.html', title='Edit expenses', form=form)

@app.route('/delete_expense/<int:id>')
def delete_expense(id):
    expense = Expenses.query.get(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('view_expenses'))
