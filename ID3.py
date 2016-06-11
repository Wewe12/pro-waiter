import math

# calculates entropy for data set for given attribute
def entropy(data, targetAttrib):
    valueFreq = {}
    dataEntropy = 0.0
    # calculate frequency for each attribute
    for record in data:
        if (valueFreq.has_key(record[targetAttrib])):
            valueFreq[record[targetAttrib]] += 1.0
        else:
            valueFreq[record[targetAttrib]] = 1.0
    # calculate entropy of data set for attribute
    for freq in valueFreq.values():
        dataEntropy += (-freq/len(data)) * math.log(freq/len(data),2)

    return dataEntropy

# calculates information gain received by data division by chosen
# attribute
def gain(data, attrib, targetAttrib):
    valueFreq = {}
    subsetEntropy = 0.0
    # calculate frequency of each attribute
    for record in data:
        if (valueFreq.has_key(record[attrib])):
            valueFreq[record[attrib]] += 1.0
        else:
            valueFreq[record[attrib]] = 1.0
    # calculate weighted average of entropy for each data subset
    # weight is a probability of set appearance in training set
    for value in valueFreq.keys():
        valueProb = valueFreq[value] / sum(valueFreq.values())
        dataSubset = [record for record in data if record[attrib] == value]
        subsetEntropy += valueProb * entropy(dataSubset, targetAttrib)
    # subtract chosen attribute's entropy from whole subset's entropy
    # then return result
    return (entropy(data, targetAttrib) - subsetEntropy)
