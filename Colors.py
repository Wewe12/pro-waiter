import Number
import Customer

# color controller

class Colors:

    def __init__(self,customers,numbers):
        self.customers = customers  # list of customers
        self.numbers = numbers  # list of table numbers (sprites)
        self.served = 0  # number of customers who received their meals

    # sends cholor change demand
    # updates number of done customers
    def update(self,index):
        state = self.customers[index].getState()
        self.numbers[index].update(state)
        if (state == 3):
            self.served += 1

    # returns number of done customers
    def getServed(self):
        return self.served
