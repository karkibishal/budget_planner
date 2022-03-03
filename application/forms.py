from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DecimalField
from wtforms.fields import DateField
from wtforms.validators import InputRequired, NumberRange, ValidationError
from datetime import date

from application.models import Categories

class IncomeForm(FlaskForm):
    select_salary = SelectField(choices=[
                            ("annual", "annual"),
                            ("monthly", "monthly"),
                            ("weekly", "weekly")
                            ])
    salary = DecimalField("Salary (£)", validators = [InputRequired(), NumberRange(min=0)])

    select_tax = SelectField(choices=[
                            ("annual", "annual"),
                            ("monthly", "monthly"),
                            ("weekly", "weekly")
                            ])
    tax = DecimalField("Tax (£)", validators = [InputRequired(), NumberRange(min=0)])

    select_ni = SelectField(choices=[
                            ("annual", "annual"),
                            ("monthly", "monthly"),
                            ("weekly", "weekly")
                            ])
    ni = DecimalField("NI contribution (£)", validators = [InputRequired(), NumberRange(min=0)])

    select_pension = SelectField(choices=[
                            ("annual", "annual"),
                            ("monthly", "monthly"),
                            ("weekly", "weekly")
                            ])
    pension = DecimalField("Pension contribution (£)", validators = [InputRequired(), NumberRange(min=0)])

    select_student_loan = SelectField(choices=[
                            ("annual", "annual"),
                            ("monthly", "monthly"),
                            ("weekly", "weekly")
                            ])
    student_loan = DecimalField("Student Loan Repayment (£)", validators = [InputRequired(), NumberRange(min=0)])

    submit = SubmitField("Submit")

class CategoriesForm(FlaskForm):
    
    name = StringField("Category", validators = [InputRequired()])
    date = DateField("Date", default = date.today, validators = [InputRequired()])
    
    submit = SubmitField("Save")



class ExpensesForm(FlaskForm):
    choices_cat = []
    for item in Categories.query.all():
        choices_cat.append(item.name)

    select_cat = SelectField("Category")
    name = StringField("Expense Description", validators = [InputRequired()])
    date = DateField("Date", default = date.today, validators = [InputRequired()])
    amount = DecimalField("Amount (£)", validators = [InputRequired(), NumberRange(min=0)])

    submit = SubmitField("Save")