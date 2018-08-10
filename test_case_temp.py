import unittest
from temp import *

class TestString(unittest.TestCase):

    def test_temp(self):
        t=Temperature()
        t.add_value()
        self.res=t.to_check_temp('500F')
        self.assertEqual(self.res,260)

    def test_temp1(self):
        t=Temperature()
        t.add_value()
        self.res=t.to_check_temp('500F')
        self.assertNotEqual(self.res,'500F')

    def test_temp2(self):
        t=Temperature()
        t.add_value()
        self.res=t.to_check_temp('-500F')
        self.assertEqual(self.res,-296)
        
    def test_min_temp(self):
        t=Temperature()
        t.add_value()
        self.min_temp=t.get_min_temp('13/12/2018')
        self.assertEqual(self.min_temp,45)

    def test_min_temp1(self):
        t=Temperature()
        t.add_value()
        self.min_temp=t.get_min_temp('12/12/2018')
        self.assertEqual(self.min_temp,34)

    def test_max_temp(self):
        t=Temperature()
        t.add_value()
        self.max_temp=t.get_max_temp('12/12/2018')
        self.assertEqual(self.max_temp,90)
        
    def test_max_temp1(self):
        t=Temperature()
        t.add_value()
        self.max_temp=t.get_max_temp('13/12/2018')
        self.assertEqual(self.max_temp,80)
        
    def test_min_temp2(self):
        t=Temperature()
        t.add_value()
        self.min_temp=t.get_min_temp('13/12/2018')
        self.assertNotEqual(self.min_temp,80)

    def test_max_temp2(self):
        t=Temperature()
        t.add_value()
        self.max_temp=t.get_max_temp('13/12/2018')
        self.assertTrue(self.max_temp,80)

    def test_avg_temp(self):
        t=Temperature()
        t.add_value()
        self.avg_temp=t.get_avg_temp('13/12/2018',[45,80,34,90])
        self.assertEqual(self.avg_temp,124.0)
        
    def test_avg_temp1(self):
        t=Temperature()
        t.add_value()
        self.avg_temp=t.get_avg_temp('12/12/2018',[34,90,45,80])
        self.assertEqual(self.avg_temp,124.0)

    def test_avg_temp2(self):
        t=Temperature()
        t.add_value()
        self.avg_temp=t.get_avg_temp('12/12/2018',[34,90,45,80])
        self.assertNotEqual(self.avg_temp,100)
        

    
if __name__=='__main__':
    unittest.main()

