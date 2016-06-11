# -*- coding: utf-8 -*-

import fuzzy.storage.fcl.Reader

class FuzzyCalc:

     
    system = fuzzy.storage.fcl.Reader.Reader().load_from_file('fuzzycalc.fcl')
    
    # preallocate input and output values
    my_input = {
        "waitinge" : 0.0,
        "meal" : 0.0,
        "distance" : 0.0
        }
    my_output = {
        "service" : 0.0
        }
 
    # if you need only one calculation you do not need the while
    # set input values
    my_input["waiting"] = float(raw_input("oczekiwanie od zamówienia (0-45) : "))
    my_input["meal"] = float(raw_input("oczekiwanie od przygotowania (0-30) : "))
    my_input["distance"] = float(raw_input("droga (0-51) : "))
    
    # calculate
    system.calculate(my_input, my_output)

    with open("machinelearning_trainingset.csv", "a") as myfile:
        myfile.write(str(my_input["waiting"]) + ";" +  str(my_input["meal"]) + ";" + str(my_input["distance"]) + ";" + str (my_output["service"]) + "\n" )

 
    # now use outputs
    print "\n obsluga : " + str( my_output["service"])
