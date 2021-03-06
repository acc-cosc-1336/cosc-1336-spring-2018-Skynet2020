import unittest

#write import for decimal to binary function
from src.assignments.assignment5 import recursive_decimal_binary

class Test_Assign5(unittest.TestCase):

    def test_sample_one(self):
        self.assertEqual(1,1)
    def test_recursive_decimal_binary_w_base_case(self):
        self.assertEqual('00000000', recursive_decimal_binary(0, 7))
    def test_recursive_decimal_binary_w_value_85(self):
        self.assertEqual('01010101', recursive_decimal_binary(85, 7))
    def test_recursive_decimal_binary_w_value_63(self):
        self.assertEqual('00111111', recursive_decimal_binary(63, 7))

unittest.main(verbosity = 2)
