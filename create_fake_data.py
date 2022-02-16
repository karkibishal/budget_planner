import random
from datetime import date
from faker import Faker
from application import db
from application.models import Expenses


def fake_data(n, datetime_start, datetime_end):
    faker = Faker()
    expense_items = ["rent", "concil tax", "electricity", "internet",
                    "mobile phone", "pet insurance", "home insurance",
                    "eating out", "takeaway", "night out", "car insurance",
                    "car loan repayment", "childcare", "baby sitter", "cinema",
                    "day out", "netflix", "amazon prime", "gym", "dentistry",
                    "haircut", "summer clothes"]
    for i in range(n):
        expense = Expenses(
                    name=faker.word(expense_items),
                    amount=random.randint(5, 50),
                    date=faker.date_between_dates(date_start=date_start, date_end=date_end),
                    categories_id=random.randint(1, 12))
        db.session.add(expense)
    db.session.commit()
    print(f'Added {n} fake data to the database.')

n = 60
date_start = date(2022, 6, 1)
date_end = date(2022, 6, 28)
fake_data(n, date_start, date_end)


