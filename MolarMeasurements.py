#import math

class Element(object):
    def __init__(self, symbol, atomicWeight):
        self.symbol = symbol
        self.atomicWeight = atomicWeight

periodicTable = []

userInputVar = NULL

"""for element in periodicTable:
    if userInputVar == element.symbol:
        #do this
        """
        

#Find how many moles the sunstance has
gramsPerMole = float(raw_input("How many grams/mole do you have in your substance? "))
gramsOfSubstance = float(raw_input("How many grams of your substance do you have? "))
moles = gramsOfSubstance / gramsPerMole
print "Your substance has %s moles" % moles

#Find the formula units in the substance
FU = moles * (6.022 * (10**23))
print "You have %s formula units of your substance" % FU

#Find how many atoms in the substance
atomsPerFU = float(raw_input("How many atoms/f.u. do you have? "))
atoms = FU * atomsPerFU
print "You have %s atoms in your substance" % atoms
