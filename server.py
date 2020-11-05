from menu import Menu

class Server(Menu):
    def __init__(self):
        super().__init__()
        self.items_ordered = []

    def orders(self):
        order_number = 0
        print("hello, these are the items we are selling today", self.items)
        while order_number < 3:
            customer_order = input("What item would you like to order?   ")

            if customer_order in self.items:
                self.items_ordered.append(customer_order)
                order_number += 1
            else:
                print("That is not a valid item")
        else:
            return print(f"you have ordered:","\n", "1)", self.items_ordered[0], "\n", "2)", self.items_ordered[1], "\n", "3)", self.items_ordered[2])
