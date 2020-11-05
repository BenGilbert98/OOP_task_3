from menu import Menu # importing menu class

class Server(Menu):
    def __init__(self):
        super().__init__() # inheriting from Menu parent class
        self.items_ordered = [] # empty list of items which will be ordered by the customer

    def orders(self):
        order_number = 0
        print("hello, these are the items we are selling today", self.items)
        while order_number < 3: # if the order number < 3 it will prompt for an order
            customer_order = input("What item would you like to order?   ")

            if customer_order in self.items: # if the input is equal to an item in the menu the items_ordered list is appended
                self.items_ordered.append(customer_order)
                order_number += 1
            else:
                print("That is not a valid item")
        else:
            return print(f"you have ordered:","\n", "1)", self.items_ordered[0], "\n", "2)", self.items_ordered[1], "\n", "3)", self.items_ordered[2]) # return statement to show orders
