from customer import Customer
#create import statement for Customer class
'''
Create an AverageCustomer class that inherits from Customer class with parameters first_name, last_name, and phone_number.
Call the Customer(superclass) constructor method and pass all the parameters including self to the method.
In the constructor method create a new class attribute named discount and set value to .03.
Create a get_discount_rate method that returns the attribute discount.
'''

class AverageCustomer(Customer):

    def __init__(self, first_name, last_name, phone_number, discount=0.03):
        Customer.__init__(self, first_name, last_name, phone_number)

        self.discount = discount

    def get_discount_rate(self, discount):
        return self.discount
