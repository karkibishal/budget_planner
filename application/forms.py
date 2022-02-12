from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, DecimalField
from wtforms.validators import DataRequired, NumberRange, ValidationError

from application.models import Income

class IncomeForm(FlaskForm):
    selection = SelectField(choices=[
                            ("annual", "annual"),
                            ("monthly", "monthly"),
                            ("weekly", "weekly")
                            ])
    annual_salary = DecimalField("Salary", 
                                validators = [DataRequired(), NumberRange(min=0)])
    tax = DecimalField("Tax")
    ni = DecimalField("NI contribution")
    pension = DecimalField("Pension contribution")
    student_loan = DecimalField("Student Loan Repayment")
    
    submit = SubmitField("Submit")

