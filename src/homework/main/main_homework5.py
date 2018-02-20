#write the import statements for homework5 functions
from homework5 import write_sales_data
from homework5 import read_sales_data

#With the functions created in homework5...
#Prompt user for number of sales records to input.
#Open a file for text writing.
#Iterate and prompt user for item name and price.
#Save item name and price to file in one line
#Calculate sum of price and write to file
#Calculate average price and write to file

#Open a file for text reading.
#Read the saved file and output table

def main():
    write_sales_data(4, 5)
    print()
    print()
    read_sales_data(1)
    

main()
