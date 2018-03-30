from invoice import Invoice
from invoice_item import InvoiceItem
#Write import statements for classes invoice and invoice_item
'''
LOOK AT THE TEST CASES FOR HINTS
Create an invoice object
Create a user controlled loop to continue until y is not typed, in loop...
    Create a new InvoiceItem
    Prompt user for description, quantity, and cost.
    Add values to the InvoiceItem.
    Add the InvoiceItem to the invoice object.
    Once user types a letter other than y display the Invoice to screen
'''

def main():
    invoice = Invoice('John', '05/23/1982')
    again = "y"
    while again.lower() == "y":
        description = input('Enter the item name: ')
        quantity = int(input('Enter the amount of the items: '))
        cost = float(input("Enter the price per unit: "))
        
        invoice_items = InvoiceItem(description, quantity, cost)
        invoice.add_invoice_item(invoice_items)

        again = input("Do you want to add another item: ")

        if again != "y":
            invoice.print_invoice()

main()
