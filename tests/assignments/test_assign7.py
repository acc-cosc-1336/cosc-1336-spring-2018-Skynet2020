import unittest
from src.assignments.assignment7 import sum_list_values
#write the import for function for assignment7 sum_list_values


class Test_Assign7(unittest.TestCase):

    def sample_test(self):
        self.assertEqual(1,1)

    def test_sum_list_values_w_list_bill_23_16_19_22(self):
        self.assertEqual(80, sum_list_values(['bill', 23, 16, 19, 22]))
    #create a test for the sum_list_values function with list elements:
    # bill 23 16 19 22

if __name__ == '__main__':
    unittest.main(verbosity=2)
