import random
from faker import Faker
from application import db
from application.models import Expenses


def fake_data(n):
    faker = Faker()
    for i in range(n):
        expense = Expenses(
                    name=faker.name(),
                    amount=random.randint(10, 300),
                    created_at=,
                    updated_at=,
                    categories_id=random.randint(1, 12))
        db.session.add(expense)
    db.session.commit()
    print(f'Added {n} fake data to the database.')