import random
import Kitchen
import Player

class Customer():

    # customer's states meaning:
    # 0 - order's hasn't placed yet (number's color: black)
    # 1 - customer is waiting for the drink and the meal (number's color: orange)
    # 2 - customer is waiting for a meal (number's color: red)
    # 3 - all done (number's color: green)

    def __init__(self,number,tilesdown,tilesup):
        self.number = number  # customer's number
        self.state = 0  # initial state
        self.tilesdown = tilesdown  # tiles above the table on which waiter is able to serve
        self.tilesup = tilesup  # tiles below the table on which waiter is able to serve
        self.doubleActionEnabled = False  # true if waiter is bringing both drink and meal


    # checking if waiter is standing on the right tile
    def actionPossible(self,player):
        direction = player.image
        if (direction == 'textures/kelUp.png'):
            if ((player.x,player.y) == self.tilesdown[0] or (player.x,player.y) == self.tilesdown[1]):
                return True
        elif (direction == 'textures/kelDn.png'):
            if ((player.x,player.y) == self.tilesup[0] or (player.x,player.y) == self.tilesup[1]):
                return True
        else:
            return False

    # allowing moving from state 1 to 3 directly (waiter is bringing both drink and meal)
    def enableDoubleAction(self):
        self.doubleActionEnabled = True

    # checking which action is possible and calling proper function 
    def customerAction(self, time, kitchen, player, colors):
        if (self.actionPossible(player) and self.state < 3):
            if (self.state == 0):
                return self.createOrder(time, kitchen, colors)
            elif (self.state == 1):
                if (self.doubleActionEnabled):
                    self.serveDrink(kitchen,colors)
                    self.doubleActionEnabled = False
                    return self.serveMeal(time, kitchen, colors)
                else:
                    return self.serveDrink(kitchen, colors)
            elif (self.state == 2):
                return self.serveMeal(time, kitchen, colors)
        else:
            return "action impossible"

    # order creating - moves from state 0 to 1 or 2 (random)
    def createOrder(self,currentTime,kitchen,colors):
        self.orderTime = currentTime
        drink = random.randint(0,1)  # customer can order drink or not
        if (drink):
            self.state = 2
            log = "Klient " + str(self.number) + " oczekuje na posilek."
        else:
            self.state = 1
            log = "Klient " + str(self.number) + " oczekuje na napoj i posilek."
        prepareTime = random.randint(20,40)  # after this time meal will be ready
        self.finishTime = prepareTime + currentTime  # at this time meal will be ready
        kitchen.orderUpdate(self)  # send order to the kitchen
        colors.update(self.number - 1)  # change number's color to orange/red
        return log

    # drink serving - moves from state 1 to 2
    def serveDrink(self, kitchen, colors):
        self.state = 2
        log = "Klient " + str(self.number) + " otrzymal napoj i oczekuje na posilek."
        kitchen.stateUpdate(self)  # send information of state change to the kitchen
        colors.update(self.number - 1)  # change number's color to red
        return log
    
    # meal serving - moves from state 2 to 3
    def serveMeal(self, time, kitchen, colors):
        if (kitchen.getMealsReadiness(time)[self.number - 1] > 0):
            self.state = 3
            log = "Klient " + str(self.number) + " obsluzony."
            kitchen.orderUpdate(self)  # send information of state change to the kitchen, delete order
            colors.update(self.number - 1)  # change number's color to green
            return log

    # getters

    def getOrderTime(self):
        if (self.state == 2 or self.state == 1):
            return self.orderTime
        else:
            print "This client isn't waiting for a meal!"

    def getFinishTime(self):
        if (self.state == 2 or self.state == 1):
            return self.finishTime
        else:
            print "This client isn't waiting for a meal!"

    def getState(self):
        return self.state

    def getNumber(self):
        return self.number
