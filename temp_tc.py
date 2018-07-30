import unittest
from temp_final import *

class TestString(unittest.TestCase):
    def test_check(self):
        t=Temperature()
        self.date=t.get_date()
        self.assertEqual(self.date,'12/11/18')

    def test_date(self):
        t=Temperature()
        self.date=t.get_date()
        self.assertNotEqual(self.date,'13/11/18')

    def test_date1(self):
        t=Temperature()
        self.date_2=t.get_user_date()
        self.assertNotEqual(self.date_2,'28-09-1998')


    def test_res(self):
        t=Temperature()
        self.res=t.get_temprtr(date)
        self.assertNotEqual(self.res,560)

    def test_dict(self):
        t=Temperature()
        self.fin_dict=t.group_temp(res,temp_val)
        self.assertNotEqual(self.fin_dict,{'12/11/2018':[[232,'500C',700]]})
        
if __name__=='__main__':
    unittest.main()

    
