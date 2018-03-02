from assignment7 import sum_list_values

'''
Create a function named process_list that calls the sum_list_values function.
Prints the list values and the sum of the element in the list as follows:
joe 10 15 20 30 40 sum: 115

Create a main function.
In the function loop as long as user wants to add another list.
Prompt the user for name and append to the list.
Prompt the user for number of numeric values in the list.
Iterate the number of times the user enters and prompt end-user for n numeric values.

Call the main function
--------------------
joe 10 15 20 30 40
bill 23 16 19 22
sue 8 22 17 14 32 17 24 21 2 9 11 17
grace 12 28 21 45 26 10
john 14 32 25 16 89

'''
def process_list(honda):
    print('This is the argument: ', honda)
    c = sum_list_values(honda)
    print(honda)
    print(c)
    

def main():
    again = 'y'
    while again == 'y':
        new_list = []
        name = input('Enter a name: ')
        new_list.append(name)
        print(new_list)
        again_2 = 'y'
        while again_2 == 'y':
            digit = int(input('Enter a number: '))
            new_list.append(digit)
            again_2 = (input('Do you want to add another number? Y/N: '))
            print(new_list)
            print()
        again = input('Do you want to create another list? Y/N: ')
    print(new_list)
    process_list(new_list)
    

main()
