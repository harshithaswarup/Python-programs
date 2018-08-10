import unittest
from spending_spree_pgrm import *

class TestString(unittest.TestCase):
    def test_bal(self):
        m=Money(1000)
        m.get_initial_balance()
        val = m.get_balance('yes',100)
        self.assertEquals(m.balance,900)

    def test_bal_1(self):
        m=Money(1000)
        m.get_initial_balance()
        val = m.get_balance('no',100)
        self.assertEquals(m.balance,1000)

    def test_bal2(self):
        m=Money(1000)
        m.get_initial_balance()
        val=m.get_balance('yes',1000)
        self.assertEqual(m.balance,0)

    def test_debt_amt(self):
        m=Money(1000)
        m.get_initial_balance()
        debt_amt=m.get_debt_amt(2000)
        self.assertEqual(debt_amt,1000)

    def test_debt_amt1(self):
        m=Money(1000)
        m.get_initial_balance()
        debt_amt=m.get_debt_amt(1400)
        self.assertEqual(debt_amt,400)

    def test_debt_amt2(self):
        m=Money(1000)
        m.get_initial_balance()
        debt_amt=m.get_debt_amt(-1400)
        self.assertEqual(debt_amt,None)

    def test_debt_amt3(self):
        m=Money(1000)
        m.get_initial_balance()
        debt_amt=m.get_debt_amt(800)
        self.assertNotEqual(debt_amt,200)
        

if __name__=='__main__':
    unittest.main()
    
        
