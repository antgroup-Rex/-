'''
unitesting with https://www.youtube.com/watch?v=1Lfv5tUGsn8&index=30&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-
'''
import unittest

def sample_func_xDouble(a):
    if type(a) not in [int,float]:
        raise TypeError("input type must be number")
    if a<0:
        raise ValueError("the input must not be negative")
    return a**0.5

class TestAUI(unittest.TestCase):
    def test_1(self):
        # test smaple
        self.assertAlmostEqual(sample_func_xDouble(9),3)
        self.assertAlmostEqual(sample_func_xDouble(1),1)
        self.assertAlmostEqual(sample_func_xDouble(0),0)
                
    def test_2(self):
        self.assertRaises(ValueError, sample_func_xDouble, -1)
        
    def test_3(self):
        self.assertRaises(TypeError, sample_func_xDouble, 1j)  # j alone is not defined
        self.assertRaises(TypeError, sample_func_xDouble, True)
        self.assertRaises(TypeError, sample_func_xDouble, "string number")
        
## test script from consule :
"""
run this script from command line :
python -m unittest test_example
for more information use :
 help (unittest.TestCase.assertSetEqual)
 
"""