import unittest

#write the import statements to bring in homework 4 functions
#valid_letter_grade, get_credit_points, get_grade_points, and get_grade_point_average
from src.homework.homework4 import sample_function
from src.homework.homework4 import valid_letter_grade
from src.homework.homework4 import get_credit_points
from src.homework.homework4 import get_grade_points
from src.homework.homework4 import get_grade_point_average

class TestHomework2(unittest.TestCase):

    def test_example(self):
        '''
        This is just an example.
        DON'T CHANGE THIS FUNCTION
        '''
        #assert that 1 equals the return value of the sample_function(1) with argument 1
        self.assertEqual(1, sample_function(1));

    #*WRITE 5 TESTS FOR get_credit_points with the letter A, B, C, D, and F as arguments

    #*WRITE 5 TESTS FOR get_credit_points with the letter a, b, c, d, and f as arguments

    #*WRITE A TEST FOR valid_letter_grade with letter B as argument

    #*WRITE A TEST FOR valid_letter_grade with letter Z as argument

    #WRITE A TEST FOR get_grade_points with arguments 3 and 4

    #WRITE A TEST FOR get_grade_point_average with arguments 9.0 and 36.0

    
    def valid_letter_grade_w_value_B(self):
        self.assertEqual('B', valid_letter_grade('B'));
    def valid_letter_grade_w_value_Z(self):
        self.assertEqual('Seems that you entered an incorect letter grade', valid_letter_grade('Z'));
    def get_credit_points_w_value_A(self):
        self.assertEqual(4, get_credit_points('A'));
    def get_credit_points_w_value_B(self):
        self.assertEqual(3, get_credit_points('B'));
    def get_credit_points_w_value_C(self):
        self.assertEqual(2, get_credit_points('C'));
    def get_credit_points_w_value_D(self):
        self.assertEqual(1, get_credit_points('D'));
    def get_credit_points_w_value_F(self):
        self.assertEqual(0, get_credit_points('F'));
    def get_credit_points_w_value_a(self):
        self.assertEqual(4, get_credit_points('a'));
    def get_credit_points_w_value_b(self):
        self.assertEqual(3, get_credit_points('b'));
    def get_credit_points_w_value_c(self):
        self.assertEqual(2, get_credit_points('c'));
    def get_credit_points_w_value_d(self):
        self.assertEqual(1, get_credit_points('d'));
    def get_credit_points_w_value_f(self):
        self.assertEqual(0, get_credit_points('f'));
    def get_grade_points_w_value_3_and_4(self):
        self.assertEqual(12, get_grade_points(3, 4));
    def get_grade_point_average_w_value_9_and_36(self):
        self.assertEqual(4.00, get_grade_point_average(9.00, 36.00));

unittest.main(verbosity = 2)
