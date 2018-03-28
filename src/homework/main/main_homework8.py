'''
Write a main function to create an empty dictionary and
a user-controlled loop to prompt for a widget name and quantity.
Add the values to the dictionary as key(widget name) and value(quantity) pairs.

After user decides to exit write data to file .

'''
from src.homework.homework8 import add_inventory, remove_inventory_widget
import pickle

def main():
    widgets = {}
    again = 'y'
    while again.lower() == 'y':
        widget_name = input('Enter a key name: ')
        quantity = int(input('Enter the value: '))
        dct = add_inventory(widget_name, quantity, widgets)
        again = input('Do you want to continue? Y/N: ')
    else:
        file_object = open('widgets_dictionary.dat', 'wb')
        pickle.dump(widgets, file_object)
        file_object.close()

main()
