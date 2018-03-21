import unittest
from src.homework.homework7 import get_p_distance_matrix
#write import statement for homework 7 file

arr = [
      ['T','T','T','C','C','A','T','T','T','A'],
      ['G','A','T','T','C','A','T','T','T','C'],
      ['T','T','T','C','C','A','T','T','T','T'],
      ['G','T','T','C','C','A','T','T','T','A']
      ]
    
result = [
         [0.0, 0.4, 0.1, 0.1],
         [0.4, 0.0, 0.4, 0.3],
         [0.1, 0.4, 0.0, 0.2],
         [0.1, 0.3, 0.2, 0.0]
         ]
class TestHomework7(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(1,1)

    #create a test for get p distance matrix with following data
    '''
    Sample Dataset
    arr = [
          ['T','T','T','C','C','A','T','T','T','A'],
          ['G','A','T','T','C','A','T','T','T','C'],
          ['T','T','T','C','C','A','T','T','T','T'],
          ['G','T','T','C','C','A','T','T','T','A']
          ]
    
    Sample Output
    0.00000 0.40000 0.10000 0.10000
    0.40000 0.00000 0.40000 0.30000
    0.10000 0.40000 0.00000 0.20000
    0.10000 0.30000 0.20000 0.00000

    '''
    
    def test_get_p_distance_matrix(self):
        self.assertEqual(result, get_p_distance_matrix(arr))

    
if __name__ == '__main__':
  unittest.main(verbosity = 2)
