import DecisionTree
import ID3

# fuzzify - to do

def fuzzifyWaiting(value):
    if (value < 11):
        return "short"
    elif (value < 29):
        return "medium"
    else:
        return "long"

def fuzzifyMeal(value):
    if (value == 0):
        return "absent"
    elif (value < 18):
        return "hot"
    else:
        return "warm"

def fuzzifyDistance(value):
    if (value < 13):
        return "close"
    elif (value < 26):
        return "medium"
    else:
        return "far"

class Classification:

    def __init__(self, file):

        fin = open(file, "r")  # training set file
        lines = [line.strip() for line in fin.readlines()]
        lines.reverse()
        attributes = [attrib.strip() for attrib in lines.pop().split(",")]
        targetAttrib = attributes[-1]
        lines.reverse()
        
        # creating data dictionary
        data = []
        for line in lines:
            data.append(dict(zip(attributes, [datum.strip() for datum in line.split(",")])))

        # creating a decision tree based on training set
        self.tree = DecisionTree.createDecisionTree(data, attributes, targetAttrib, ID3.gain)

    def classify(self, customers):
        # creating test data
            
        table = []
        for i in range(len(customers)):
            collection = {}
            collection['Waiting'] = fuzzifyWaiting(customers[i][0])
            collection['Meal'] = fuzzifyMeal(customers[i][1])
            collection['Distance'] = fuzzifyDistance(customers[i][2])
            table.append(collection)

        # classyfing test data
        classification = DecisionTree.classify(self.tree,table)
        table1=[]
        for item in classification:
            table1.append(item)

        return table1

