#write import statement for reverse string function
from exam import reverse_string
'''
10 points
Write a main function to ....
Loop as long as user types y.
Prompt user for a string (assume user will always give you good data).
Pass the string to the reverse string function and display the reversed string

'''
def main():
    again = 'y'
    while again == 'y':
        string = input('Enter a string here: ')
        var = reverse_string(string)
        print(var)
        again = input('Do you want to continue? y/n: ')      
