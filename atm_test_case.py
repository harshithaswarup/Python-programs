import unittest
from atm_task_1 import *

class TestString(unittest.TestCase):
    def test_balance(self):
        a=Atm(100000,'Harshi',0001)
        self.bal=a.get_deposited_bal(50000)
        self.assertEqual(self.bal,150000)

    def test_balance1(self):
        a=Atm(100000,'Harshi',0001)
        self.bal=a.get_deposited_bal(-5000)
        self.assertEqual(self.bal,95000)

    def test_balance2(self):
        a=Atm(1000,'Harshi',0001)
        self.bal=a.get_deposited_bal(-500)
        self.assertEqual(self.bal,500)
        
    def test_balance3(self):
        a=Atm(1000,'Harshi',0001)
        self.bal=a.get_deposited_bal(500)
        self.assertTrue(self.bal,1500)

    def test_balance4(self):
        a=Atm(100000,'Harshi',0001)
        self.bal=a.get_deposited_bal(50000)
        self.assertNotEqual(self.bal,15000)

    def test_check_bal(self):
        a=Atm(100000,'Harshi',0001)
        self.bal=a.get_withdrawed_balance(50000)
        self.assertEqual(self.bal,50000)

    def test_check_balance(self):
        a=Atm(1000,'Harshi',0001)
        self.bal=a.get_withdrawed_balance(100)
        self.assertEqual(self.bal,900)

    def test_check_balance1(self):
        a=Atm(1000,'Harshi',0001)
        self.bal=a.get_withdrawed_balance(-100)
        self.assertEqual(self.bal,1100)

    def test_check_balance2(self):
        a=Atm(100000,'Harshi',0001)
        self.bal=a.get_withdrawed_balance(100000)
        self.assertEqual(self.bal,0)

    def test_check_balance3(self):
        a=Atm(100000,'Harshi',0001)
        self.bal=a.get_withdrawed_balance(100)
        self.assertNotEqual(self.bal,100000)


    
if __name__=='__main__':
    unittest.main()

