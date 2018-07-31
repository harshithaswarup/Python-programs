import unittest
from hotel_room_booking import *

class TestString(unittest.TestCase):
    
    def test_date(self):
        r=Room()
        self.check_in_date=r.get_room_cost()
        self.assertNotEqual(self.check_in_date,2018-8-12)

    def test_cost(self):
        r=Room()
        self.discount_amt=r.get_discount(1200,0.5)
        self.assertEqual(self.discount_amt,600)
        
    def test_cost1(self):
        r=Room()
        self.discount_amt=r.get_discount(1100,0.5)
        self.assertNotEqual(self.discount_amt,600)

    def test_cost2(self):
        r=Room()
        self.discount_amt=r.get_discount(1100,-0.10)
        self.assertNotEqual(self.discount_amt,1000)

    def test_cust(self):
        r=Room()
        self.cust_type=r.get_cust_details()
        self.cust_type_1=['Normal','Reward']
        self.assertEqual(self.cust_type,self.cust_type_1)

    def test_cust1(self):
        r=Room()
        self.cust_type=r.get_cust_details()
        self.cust_type_1=['Reward','Reward']
        self.assertNotEqual(self.cust_type,self.cust_type_1)

    def test_fincost(self):
        r=Room()
        self.discount_cost=r.get_final_cost(1000,0.5,cust_type=['Normal','Regular'])
        self.assertNotEqual(self.discount_cost,1140)


    
if __name__=='__main__':
    unittest.main()
