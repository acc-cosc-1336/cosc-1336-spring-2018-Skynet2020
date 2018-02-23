#write the import for the function get_count_A_C_G_and_T_in_string from assignment 6 file
from assignment6 import get_count_A_C_G_and_T_in_string

'''
Using function get_count_A_C_G_and_T_in_string create a main function and...
Call the function get_count_A_C_G_and_T_in_string from assignment 6 file
With the string AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC as an argument
Sample Output:

DNA String:
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
A 20, C 12, G 17, T 21


Call the main function in Python Shell or in this file.
'''

def main():
    

##    get_count_A_C_G_and_T_in_string('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
    count_A, count_C, count_G, count_T = get_count_A_C_G_and_T_in_string('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
    print('DNA string: ')
    print('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
    print('A', count_A, 'C', count_C, 'G', count_G, 'T', count_T)
    

main()
