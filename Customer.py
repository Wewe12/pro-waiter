import random
import Kitchen
import Player

class Customer():

    def __init__(self,number,tilesdown,tilesup):
        self.number = number
        self.state = 0
        self.tilesdown = tilesdown
        self.tilesup = tilesup

    def createOrder(self,currentTime,kitchen):
        self.orderTime = currentTime
        drink = random.randint(0,1)
        if (drink):
            self.state = 2
            log = "Klient " + str(self.number) + " oczekuje na posilek."
        else:
            self.state = 1
            log = "Klient " + str(self.number) + " oczekuje na napoj i posilek."
        prepareTime = random.randint(20,40)
        self.finishTime = prepareTime + currentTime
        kitchen.update(self)
        return log

    def serveDrink(self):
        self.state = 2
        log = "Klient " + str(self.number) + " otrzymal napoj i oczekuje na posilek."
        return log
    
    def serveMeal(self, time, kitchen):
        if (kitchen.getMealsReadiness(time)[self.number - 1] > 0):
            self.state = 3
            log = "Klient " + str(self.number) + " obsluzony."
            return log

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

    def customerAction(self, time, kitchen, player):
        if (self.actionPossible(player) and self.state < 3):
            if (self.state == 0):
                return self.createOrder(time, kitchen)
            elif (self.state == 1):
                return self.serveDrink()
            elif (self.state == 2):
                return self.serveMeal(time, kitchen)
        else:
            return "action impossible"

    def getOrderTime(self):
        if (self.state == 2 or self.state == 1):
            return self.orderTime
        else:
            print "This client isn't waiting for a meal! \n"

    def getFinishTime(self):
        if (self.state == 2 or self.state == 1):
            return self.finishTime
        else:
            print "This client isn't waiting for a meal! \n"

    def getState(self):
        return self.state

    def getNumber(self):
        return self.number
