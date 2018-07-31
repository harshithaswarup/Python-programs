import unittest
from spending_spree import *

class TestString(unittest.TestCase):
    def test_init_bal(self):
        m=Money()
        self.balance=m.get_initial_balance()
        self.assertEqual(self.balance,1000)

    def test_init_bal_1(self):
        m=Money()
        self.balance=m.get_initial_balance()
        self.assertNotEqual(self.balance,1000)

    def test_balance(self):
        m=Money()
        self.item_cost=m.get_item_cost()
        self.assertNotEqual(self.item_cost,200)

    def test_check1(self):
        m=Money()
        self.sub_balance=m.get_balance(item_cost,x,user_choice,balance)
        self.assertNotEqual(self.sub_balance,-300)
    
        
    def test_debt(self):
        m=Money()
        self.debt_amt=m.get_debt_amount(300,200)
        self.assertEqual(self.debt_amt,100)

    def test_debt_1(self):
        m=Money()
        self.debt_amt=m.get_debt_amount(500,200)
        self.assertNotEqual(self.debt_amt,-300)
        

if __name__=='__main__':
    unittest.main()
    
        
