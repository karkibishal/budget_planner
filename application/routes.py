from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Income
from application.forms import IncomeForm

@app.route('/income', methods=['POST', 'GET'])
def income():
    form = IncomeForm()
    if form.validate_on_submit():
        income = Income(
            annual_salary = form.annual_salary.data,
            tax = form.tax.data,
            ni = form.ni.data,
            pension = form.pension.data,
            student_loan = form.student_loan.data
        )
        db.session.add(income)
        db.session.commit()
        return redirect(url_for('income'))
    return render_template('income.html', title="Add income details", form=form)
