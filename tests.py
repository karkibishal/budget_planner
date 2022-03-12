from flask_testing import TestCase
import unittest
from application import app, db, routes
from application.models import Categories, Expenses, Income

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
            DEBUG=True,
            TESTING=True,
            WTF_CSRF_ENABLES=False
            )
        return app

    def setUp(self):
        db.drop_all()
        db.create_all()
        cat1 = Categories(id=1, name="Household")
        expense1 = Expenses(id=1, name="water", amount=120,categories_id=1)
        db.session.add(cat1)
        db.session.add(expense1)
        db.session.commit()
              

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestGetResponse(TestBase):

    def test_index_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Budget Planner Dashboard', response.data)

    def test_income_get(self):
       response = self.client.get('/income')
       self.assertEqual(response.status_code,200)
       self.assertIn(b'Add income details', response.data)

    def test_add_expense_get(self):
        response = self.client.get('/add_expense')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Add expense items', response.data)

    def test_add_category_get(self):
        response = self.client.get('/add_category')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'Add expense categories', response.data)

    def test_view_expense_get(self):
        response = self.client.get('/view_expenses')
        self.assertEqual(response.status_code,200)
        
    def test_view_category_get(self):
        response = self.client.get('/view_category')
        self.assertEqual(response.status_code,200)

    def test_edit_expense_get(self):
        response = self.client.get('/edit_expense/1')
        self.assertEqual(response.status_code,200)
        
    def test_edit_category_get(self):
        response = self.client.get('/edit_category/1')
        self.assertEqual(response.status_code,200)
        
    def test_delete_expense_get(self):
        response = self.client.get('/delete_expense/1')
        self.assertEqual(response.status_code,302)
        
            
class TestPostResponse(TestBase):

    def test_add_category(self):
        response = self.client.post('/add_category',
                    data = {'id':2, 
                        'name':'Utilities'})
        self.assertEqual(response.status_code, 200)
        test = Categories.query.filter_by(id=2).first()
        assert test.id == 2
        assert test.name == "Utilities"

    def test_add_expense(self):
        response = self.client.post('/add_expense',
                    data = {'id':2, 
                        'name':'water',
                        'amount': 120})
        self.assertEqual(response.status_code, 200)
        test = Categories.query.filter_by(id=2).first()
        assert test.id == 2
        assert test.name == "water"
        assert test.amount == 120
                        
    def test_delete_category(self):
        response = self.client.post('/delete_category/1',
                                    data = {'id' : 1})
        self.assertEqual(response.status_code, 200)

    def test_delete_expense(self):
        response = self.client.post('/delete_expense/1',
                                    data = {'id' : 1})
        self.assertEqual(response.status_code, 200)

    def test_edit_category(self):
        response = self.client.post('/edit_category/1',
                                    data = {'id' : 1})
        self.assertEqual(response.status_code, 200)

    def test_income(self):
        response = self.client.post('/income',
                    data = {'salary':25000, 
                        'tax':0,
                        'ni':0,
                        'pension':0,
                        'student_loan':0})   
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()