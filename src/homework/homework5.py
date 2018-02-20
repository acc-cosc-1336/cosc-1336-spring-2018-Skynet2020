#Create a function named write_sales_data with file_object, item and price as parameters.
#The function should write item and price to a file.

#Create another function named read_sales_data with file_object as a parameter.
#The function will read the file line by line and display to screen to produce the table described in homework 5.

def write_sales_data(item, price):
    outfile = open('file_object.txt', 'w')

    price_1 = float(input('Enter the price for the item 1: '))
    price_2 = float(input('Enter the price for the item 2: '))
    price_3 = float(input('Enter the price for the item 3: '))
    
    total_price = price_1 + price_2 + price_3
    average_price = (price_1 + price_2 + price_3)/3
    outfile.write('Item'+\
                  '\t'+\
                  'Price\n')
    outfile.write('Hamburger' +\
                  '\t'+\
                  str(price_1)+\
                  '\n')
    outfile.write('Fries'+\
                  '\t'+\
                  str(price_2)+\
                  '\n')
    outfile.write('Drink'+\
                  '\t'+\
                  str(price_3)+\
                  '\n')
    outfile.write('Total'+\
                  '\t'+\
                  str(total_price)+\
                  '\n')
    outfile.write('Avg Price'+\
                  '\t'+\
                  format(average_price, '.2f')+\
                  '\n')
    
    outfile.close()
    print('Data written to the file')

def read_sales_data(file_object):
    infile = open('file_object.txt', 'r')

    action_1 = str(infile.readline())
    action_2 = str(infile.readline())
    action_3 = str(infile.readline())
    action_4 = str(infile.readline())
    action_5 = str(infile.readline())
    action_6 = str(infile.readline())

    infile.close

    print(action_1)
    print(action_2)
    print(action_3)
    print(action_4)
    print(action_5)
    print(action_6)
