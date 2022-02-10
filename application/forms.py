from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, DecimalField
from wtforms.validators import DataRequired, ValidationError

from application.models import Income

class IncomeForm(FlaskForm):
    annual_salary = DecimalField("Annual Salary")
    tax = DecimalField("Tax")
    ni = DecimalField("NI contribution")
    pension = DecimalField("Pension contribution")
    student_loan = DecimalField("Student Loan Repayment")
    
    submit = SubmitField("Submit")

