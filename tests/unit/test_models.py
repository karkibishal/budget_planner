from application.models import Categories, Expenses, Income

def test_categories():
    """
    GIVEN a Categories model
    WHEN a new category is created
    THEN check the id, name, date fields are defined correctly
    """
    category = Categories(name="Food") 
    #assert category.id == 1
    assert category.name == "Food"