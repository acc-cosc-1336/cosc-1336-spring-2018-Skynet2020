import unittest
from src.homework.homework9 die import Die
#Write the import statement for the Die class

class TestHomework9(unittest.TestCase):

    sideup = Die()
    
    def test_rolls_values_1_to_6(self):
        '''
        Write a test case to ensure that the Die class only rolls values from 1 to 6

        '''
        sideup = Die()
        self.assertTrue(0 < sideup.roll() < 7)



if __name__ == '__main__':
  unittest.main(verbosity = 2)
