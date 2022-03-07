from application import db
from application.models import Categories


db.create_all()

"""
category_objects = [
        Categories(name = "Household"),
        Categories(name = "Utilities"),
        Categories(name = "Food"),
        Categories(name = "Repayments"),
        Categories(name = "Transport"),
        Categories(name = "Subscriptions"),
        Categories(name = "Family"),
        Categories(name = "Entertainment"),
        Categories(name = "Health"),
        Categories(name = "Clothes"),
        Categories(name = "Holiday/One off"),
        Categories(name = "Miscellaneous")
        ]

db.session.add_all(category_objects)
db.session.commit()
"""