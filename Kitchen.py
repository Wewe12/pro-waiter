import Customer

class Kitchen():

    def __init__(self, number):
        self.number = number  # number of customers
        self.customerStates = [0 for i in range(number)]  # list that represents each customer's state
        self.orderTimes = [0 for i in range(number)]  # list that represents each customer's time of order placing
        self.orderFinishTimes = []  # list which tells when each already ordered meal will be ready
        self.waitingMeals = [0 for i in range(number)]  # list which tells what time the meal was finished

    # update customer's state on the list
    def stateUpdate(self, customer):
        index = customer.getNumber() - 1
        currentState = customer.getState()
        self.customerStates[index] = currentState
    
    # update customer's state on the list
    # update informations of order timing
    def orderUpdate(self, customer):
        index = customer.getNumber() - 1
        currentState = customer.getState()
        self.customerStates[index] = currentState
        if (currentState == 1 or currentState == 2):
            self.orderTimes[index] = customer.getOrderTime()
            finishTime = customer.getFinishTime()
            self.orderFinishTimes.append((finishTime,index))
            self.orderFinishTimes = sorted(self.orderFinishTimes, key=lambda x: x[0])
        else:
            self.orderTimes[index] = 0
            self.waitingMeals[index] = 0

    # sends information of meal readiness, saves current time
    def makeMealReady(self,customer,time):
        index = customer.getNumber() - 1
        self.waitingMeals[index] = time
        log = "Posilek klienta " + str(index + 1) + " jest gotowy."
        return log

    # returns list which tells how much time elapsed from each
    # meal preparing finish (0 if not finished yet)
    def getMealsReadiness(self,currentTime):
        timeList = []
        for i in range(self.number):
            if (self.waitingMeals[i] > 0):
                timeList.append(currentTime - self.waitingMeals[i])
            else:
                timeList.append(0)
        return timeList

    # deleting finished meal from the timing list
    def removeTimeEvent(self):
        self.orderFinishTimes.pop(0)

    # checking if any meal is ready, returns the lowest possible
    # customer's number if so
    def anyMealReady(self):
        for i in range(len(self.waitingMeals)):
            if (self.waitingMeals[i] > 0):
                return i+1
        return 0
