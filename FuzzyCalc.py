import fuzzy.storage.fcl.Reader

class FuzzyCalc:

    system = fuzzy.storage.fcl.Reader.Reader().load_from_file("./obsluga.fcl")
 
    # preallocate input and output values
    my_input = {
        "oczekiwanie" : 0.0,
        "jedzenie" : 0.0,
        "droga" : 0.0
        }
    my_output = {
        "obsluga" : 0.0
        }
 
    # if you need only one calculation you do not need the while
    # set input values
    my_input["oczekiwanie"] = float(raw_input("oczekiwanie: "))
    my_input["jedzenie"] = float(raw_input("jedzenie: "))
    my_input["droga"] = float(raw_input("droga: "))
    
    # calculate
    system.calculate(my_input, my_output)
 
    # now use outputs
    print "obsluga: " + str( my_output["obsluga"])
