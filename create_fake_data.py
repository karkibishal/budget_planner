import random
from datetime import datetime
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
                    amount=random.randint(20, 600),
                    created_at=faker.date_time_between_dates(datetime_start=datetime_start, datetime_end=datetime_end),
                    updated_at=faker.date_time_between_dates(datetime_start=datetime_start, datetime_end=datetime_end),
                    categories_id=random.randint(1, 12))
        db.session.add(expense)
    db.session.commit()
    print(f'Added {n} fake data to the database.')

n = 50
datetime_start = datetime(2021, 12, 1)
datetime_end = datetime(2021, 12, 30)
fake_data(n, datetime_start, datetime_end)