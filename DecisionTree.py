# building new decision tree and classification training data

# makes a list of every value of specific attribute
def majorityValue(data, targetAttrib):
    data = data[:]
    return mostFrequent([record[targetAttrib] for record in data])

# returns most frequent attribute from the list
def mostFrequent(lst):
    lst = lst[:]
    highestFreq = 0
    mostFreq = None
    for value in unique(lst):
        if (lst.count(value) > highestFreq):
            mostFreq = value
            highestFreq = lst.count(value)
    return mostFreq

# returns a list without multiple elements
def unique(lst):
    lst = lst[:]
    uniqueList = []

    for element in lst:
        if (uniqueList.count(element) <= 0):
            uniqueList.append(element)

    return uniqueList

# builds a list of values for given attribute for each recors in data
# set, deleting multiple values
def getValues(data, attrib):
    data = data [:]
    return unique([record[attrib] for record in data])

# from all available attributes chooses the one with biggest
# information gain or smallest entropy
def chooseAttribute(data, attributes, targetAttrib, fitness):
    data = data [:]
    bestGain = 0.0
    bestAttrib = None
    for attrib in attributes:
        gain = fitness(data, attrib, targetAttrib)
        if (gain >= bestGain and attrib != targetAttrib):
            bestGain = gain
            bestAttrib = attrib
    return bestAttrib

# returns a list of every record that value for given attribute
# matches pattern
def getExamples(data, attrib, value):
    data = data [:]
    rtnList = []

    if (not data):
        return rtnList
    else:
        record = data.pop()
        if (record[attrib] == value):
            rtnList.append(record)
            rtnList.extend(getExamples(data, attrib, value))
            return rtnList
        else:
            rtnList.extend(getExamples(data, attrib, value))
            return rtnList

# recursive searches the decision tree and returns
# classification for given record
def getClassification(record, tree):
    # if node is a string, then it's a leaf
    if type(tree) == type("string"):
        return tree
    else:
        attrib = tree.keys()[0]
        t = tree[attrib][record[attrib]]
        return getClassification(record, t)

# return classification list for each record from data list based on
# decision tree
def classify(tree, data):
    data = data [:]
    classification = []
    for record in data:
        classification.append(getClassification(record, tree))
    return classification

# returns a new decision tree based on training set
def createDecisionTree(data, attributes, targetAttrib, fitnessFunc):
    data = data[:]
    values = [record[targetAttrib] for record in data]
    default = majorityValue(data, targetAttrib)
    # if data or attributes set is empty, return default
    if ((not data) or (len(attributes) - 1 <= 0)):
        return default
    # if each record in set has the same classification, return it
    elif (values.count(values[0]) == len(values)):
        return values[0]
    else:
        # choose next attribute for classifying data
        best = chooseAttribute(data, attributes, targetAttrib, fitnessFunc)
        # build new decision tree based on best attribute as empty
        # dictionary
        tree = {best:{}}
        # build new subtree for each value of best attribute
        for value in getValues(data, best):
            # create subtree for given value with next best attribute
            subtree = createDecisionTree(getExamples(data, best, value), [attrib for attrib in attributes if attrib != best], targetAttrib, fitnessFunc)
            # add new subtree to dictionary
            tree[best][value] = subtree
    return tree
