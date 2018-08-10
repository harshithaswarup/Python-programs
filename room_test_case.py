import unittest
from hotel_room_booking import *

class TestString(unittest.TestCase):
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

    def test_total_cost(self):
        r=Room()
        self.total_cost=r.get_total_cost(2,500,600,2)
        self.assertEqual(self.total_cost,1000)

    def test_total_cost1(self):
        r=Room()
        self.total_cost=r.get_total_cost(2,500,600,5)
        self.assertEqual(self.total_cost,1200)

    def test_total_cost2(self):
        r=Room()
        self.total_cost=r.get_total_cost(2,500,600,4)
        self.assertNotEqual(self.total_cost,1200)

    def test_final_cost(self):
        r=Room()
        self.discount_cost=r.get_final_cost(1200,500,'Reward')
        self.assertEqual(self.discount_cost,700)

    def test_final_cost1(self):
        r=Room()
        self.discount_cost=r.get_final_cost(1000,500,'Reward')
        self.assertEqual(self.discount_cost,None)

    def test_final_cost2(self):
        r=Room()
        self.discount_cost=r.get_final_cost(1200,500,'Reward')
        self.assertNotEqual(self.discount_cost,1200)

    def test_final_cost3(self):
        r=Room()
        self.discount_cost=r.get_final_cost(1200,500,'Normal')
        self.assertEqual(self.discount_cost,None)

    
        
        
if __name__=='__main__':
    unittest.main()
