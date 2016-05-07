import Customer

class Kitchen():

    def __init__(self, number):
        self.number = number
        self.customerStates = [0 for i in range(number)]
        self.orderTimes = [-1 for i in range(number)]
        self.orderFinishTimes = []
        self.waitingMeals = [-1 for i in range(number)]

    def update(self, customer):
        index = customer.getNumber() - 1
        currentState = customer.getState()
        finishTime = customer.getFinishTime()
        if (currentState == 1 or currentState == 2):
            self.orderTimes[index] = customer.getOrderTime()
            self.orderFinishTimes.append((finishTime,index))
            self.orderFinishTimes = sorted(self.orderFinishTimes, key=lambda x: x[0])
        else:
            self.orderTimes[index] = -1
            self.waitingMeals[index] = -1
        self.customerStates[index] = currentState

    def makeMealReady(self,customer,time):
        index = customer.getNumber() - 1
        self.waitingMeals[index] = time
        log = "Posilek klienta " + str(index + 1) + " jest gotowy."
        return log

    def getMealsReadiness(self,currentTime):
        timeList = []
        for i in range(self.number):
            if (self.waitingMeals[i] > 0):
                timeList.append(currentTime - self.waitingMeals[i])
            else:
                timeList.append(0)
        return timeList

    def removeTimeEvent(self):
        self.orderFinishTimes.pop(0)

    def anyMealReady(self):
        for i in range(len(self.waitingMeals)):
            if (self.waitingMeals[i] > 0):
                return i
        return 0
