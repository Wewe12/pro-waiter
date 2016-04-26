# -*- coding: utf-8 -*-

import fuzzy.storage.fcl.Reader

class FuzzyCalc:

    system = fuzzy.storage.fcl.Reader.Reader().load_from_file("./fuzzycalc.fcl")
 
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
    my_input["oczekiwanie"] = float(raw_input("oczekiwanie od zamówienia (0-10) : "))
    my_input["jedzenie"] = float(raw_input("oczekiwanie od przygotowania (0-10) : "))
    my_input["droga"] = float(raw_input("droga (0-10) : "))
    
    # calculate
    system.calculate(my_input, my_output)
 
    # now use outputs
    print "\n obsługa : " + str( my_output["obsluga"])
