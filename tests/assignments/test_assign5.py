import unittest

#write import for decimal to binary function
from assignment5 import recursive_decimal_binary

class Test_Assign5(unittest.TestCase):

    def test_sample_one(self):
        self.assertEqual(1,1)
    def test_recursive_decimal_binary_w_base_case(self):
        self.assertEqual('00000000', recursive_decimal_binary(0, 7))

unittest.main(verbosity = 2)
    
    #write test cases with arguments 85 and 63 for recursive_decimal_binary function


