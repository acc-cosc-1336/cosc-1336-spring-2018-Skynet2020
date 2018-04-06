#Write import statements for classes invoice and invoice_item and PRODUCT
from product import Product
from customer import Customer
from invoice import Invoice
from invoice_item import InvoiceItem

##src.assignments.assignment10.
##src.assignments.assignment10.

#ASSIGNMENT10 Write import statements for classes product and customer


'''
LOOK AT THE TEST CASES FOR HINTS
Create an invoice object 

In the loop:
Create a user controlled loop to continue until y is not typed, in loop...
    Prompt user for description, quantity, and cost.
    Create a new InvoiceItem, use the newly created product as a parameter argument 
    Add values to the InvoiceItem.
    Add the InvoiceItem to the invoice object.
    Once user types a letter other than y display the Invoice to screen
'''
#ASSIGNMENT10: Make sure to change invoice bill_to argument to an instance of a Customer class 


first = input('Enter customer first name: ')
last = input('Enter customer last name: ')
phone_number = input('Enter customer\'s phone number: ')
customer = Customer(first, last, phone_number)

invoice = Invoice(customer, '03012018')

keep_going = 'y'

while keep_going == 'y':

    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    cost = float(input("Enter cost: "))
    product = Product(777, cost, name)
    
    #ASSIGNMENT10: Create a product object and add description and cost as parameter arguments.
    #Quantity parameter remains same.
    invoice.add_invoice_item(InvoiceItem(quantity, product))

    keep_going = input("Enter another type y: ")
    print()


invoice.print_invoice()
