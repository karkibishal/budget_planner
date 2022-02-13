from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, DecimalField
from wtforms.validators import InputRequired, NumberRange, ValidationError

from application.models import Categories

class IncomeForm(FlaskForm):
    select_salary = SelectField(choices=[
                            ("annual", "annual"),
                            ("monthly", "monthly"),
                            ("weekly", "weekly")
                            ])
    salary = DecimalField("Salary", validators = [InputRequired(), NumberRange(min=0)])

    select_tax = SelectField(choices=[
                            ("annual", "annual"),
                            ("monthly", "monthly"),
                            ("weekly", "weekly")
                            ])
    tax = DecimalField("Tax", validators = [InputRequired(), NumberRange(min=0)])

    select_ni = SelectField(choices=[
                            ("annual", "annual"),
                            ("monthly", "monthly"),
                            ("weekly", "weekly")
                            ])
    ni = DecimalField("NI contribution", validators = [InputRequired(), NumberRange(min=0)])

    select_pension = SelectField(choices=[
                            ("annual", "annual"),
                            ("monthly", "monthly"),
                            ("weekly", "weekly")
                            ])
    pension = DecimalField("Pension contribution", validators = [InputRequired(), NumberRange(min=0)])

    select_student_loan = SelectField(choices=[
                            ("annual", "annual"),
                            ("monthly", "monthly"),
                            ("weekly", "weekly")
                            ])
    student_loan = DecimalField("Student Loan Repayment", validators = [InputRequired(), NumberRange(min=0)])
    
    submit = SubmitField("Submit")

choices_cat = []
for item in Categories.query.all():
    choices_cat.append((item.name, item.name))

class ExpensesForm(FlaskForm):
    
    select_cat = SelectField("Category", choices=choices_cat)
    name = StringField("Expense Description", validators = [InputRequired()])
    amount = DecimalField("Amount (£)", validators = [InputRequired(), NumberRange(min=0)])

    submit = SubmitField("Add")