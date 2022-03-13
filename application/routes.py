from flask import render_template, url_for, redirect, request
from application import app, db
from datetime import timedelta, date
from application.models import Income, Categories, Expenses
from application.forms import IncomeForm, ExpensesForm, CategoriesForm
from application.chart_func import weeklyExpense, categoricalExpense, monthlyExpense

@app.route('/', methods=['POST', 'GET'])
def index():

    # expenses in the current week line chart
    weekly_expense =  weeklyExpense()          

    # expense category percentage in a month doughnut chart
    category_names, categorical_expense = categoricalExpense() 
    
    # total expense months comparison bar chart
    monthly_expense = monthlyExpense()
    
    return render_template('index.html', title="Budget Tracker Dashboard", weekly_expense=weekly_expense, category_names=category_names, 
                            categorical_expense=categorical_expense, monthly_expense=monthly_expense)


@app.route('/income', methods=['POST', 'GET'])
def income():
    form = IncomeForm()
    if form.validate_on_submit():
        if form.select_salary.data == "annual":
            salary = form.salary.data / 12
        elif form.select_salary.data == "monthly":
            salary = form.salary.data
        elif form.select_salary.data == "weekly":
            salary = form.salary.data * 4.33

        if form.select_tax.data == "annual":
            tax = form.tax.data / 12
        elif form.select_tax.data == "monthly":
            tax = form.tax.data 
        elif form.select_tax.data == "weekly":
            tax = form.tax.data * 4.33

        if form.select_ni.data == "annual":
            ni = form.ni.data / 12
        elif form.select_ni.data == "monthly":
            ni = form.ni.data 
        elif form.select_ni.data == "weekly":
            ni = form.ni.data * 4.33
            
        if form.select_pension.data == "annual":
            pension = form.pension.data / 12
        elif form.select_pension.data == "monthly":
            pension = form.pension.data 
        elif form.select_pension.data == "weekly":
            pension = form.pension.data * 4.33

        if form.select_student_loan.data == "annual":
            student_loan = form.student_loan.data / 12
        elif form.select_student_loan.data == "monthly":
            student_loan = form.student_loan.data 
        elif form.select_student_loan.data == "weekly":
            student_loan = form.student_loan.data * 4.33

        take_home_pay = salary - tax - ni - pension - student_loan
        
        income = Income(
                    salary = salary,
                    tax = tax,
                    ni = ni,
                    pension = pension,
                    student_loan = student_loan,
                    take_home_pay = take_home_pay
                    )
        
        db.session.add(income)
        db.session.commit()
        return redirect(url_for('income'))

    latest_income = Income.query.order_by(Income.id.desc()).first()
    if latest_income == None:
        monthly_pay = 0
    else:
        monthly_pay = latest_income.take_home_pay
    return render_template('income.html', title="Add income details", form=form, monthly_pay=monthly_pay)


@app.route('/add_category', methods=['POST', 'GET'])
def add_category():
    form = CategoriesForm()
    if form.validate_on_submit():
        category = Categories(
                    name = form.name.data,
                    date = form.date.data,
                    )
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('add_category'))
    return render_template('add_category.html', title="Add expense categories", form=form)

@app.route('/view_category', methods=['POST', 'GET'])
def view_category():
    all_categories = Categories.query.all()
    return render_template('view_category.html', title="View categories", all_categories=all_categories)

@app.route('/edit_category/<int:id>', methods=['GET', 'POST'])
def edit_category(id):
    category = Categories.query.get(id)
    form = CategoriesForm(name = category.name, date = category.date)
    if form.validate_on_submit():
        category.name = form.name.data
        category.date = form.date.data
        db.session.commit()
        return redirect(url_for('view_category'))
    elif request.method == 'GET':
        form = form
    return render_template('edit_category.html', title='Edit expense categories', form=form)

@app.route('/delete_category/<int:id>')
def delete_category(id):
    category = Categories.query.get(id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('view_category'))


@app.route('/add_expense', methods=['POST', 'GET'])
def add_expense():
    choices_cat = []
    for item in Categories.query.all():
        choices_cat.append(item.name)
    
    form = ExpensesForm()
    form.select_cat.choices = choices_cat
    if form.validate_on_submit():
        expense = Expenses(
                    name = form.name.data,
                    amount = form.amount.data,
                    date = form.date.data,
                    categories_id = Categories.query.filter_by(name=form.select_cat.data).first().id
                    )
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('add_expense'))
    return render_template('add_expense.html', title="Add expense items", form=form)

@app.route('/view_expenses', methods=['POST', 'GET'])
def view_expenses():
    all_expenses = Expenses.query.all()
    return render_template('view_expenses.html', title="View expenses", all_expenses=all_expenses)

@app.route('/edit_expense/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    expense = Expenses.query.get(id)
    choices_cat = []
    for item in Categories.query.all():
        choices_cat.append(item.name)

    form = ExpensesForm(name = expense.name, select_cat = expense.category.name, 
                        amount = expense.amount, date = expense.date)
    form.select_cat.choices = choices_cat
    if form.validate_on_submit():
        expense.name = form.name.data
        expense.amount = form.amount.data
        expense.categories_id = Categories.query.filter_by(name=form.select_cat.data).first().id
        expense.date = form.date.data
        db.session.commit()
        return redirect(url_for('view_expenses'))
    elif request.method == 'GET':
        form = form
    return render_template('edit_expense.html', title='Edit expense items', form=form)

@app.route('/delete_expense/<int:id>')
def delete_expense(id):
    expense = Expenses.query.get(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('view_expenses'))
