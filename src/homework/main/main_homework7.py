from src.homework.homework7 import get_p_distance_matrix, print_get_p_distance_matrix
'''
Write a main function to...
Read p_distance.dat file
From the file data, create a two-dimensional list like the following example:

[
 ['T','T','T','C','C','A','T','T','T','A'],
 ['G','A','T','T','C','A','T','T','T','C'],
 ['T','T','T','C','C','A','T','T','T','T'],
 ['G','T','T','C','C','A','T','T','T','A']
]

Pass the list to the get_p_distance_matrix function as an argument
Display the p distance matrix to screen
'''
def main():
    matrix = []
    file_object = open('p_distance.dat', 'r')
    content = file_object.readlines()
    for line in content[:]:
        line = line.rstrip('\n').replace(" ", "")
        matrix_line = []
        for letter in line:
            matrix_line.append(letter)
        matrix.append(matrix_line)
    results_mtrx = get_p_distance_matrix(matrix)
    print_get_p_distance_matrix(results_mtrx)

main()
