#import math

class Element (object):
    def __init__ (self, symbol, atomicNumber, atomicWeight):
        self.symbol = symbol
        self.atomicNumber = atomicNumber
        self.atomicWeight = atomicWeight

periodicTable = [
  	#Just including stuff on data table for lab
	oxygen = Element("O", 8, 15.9994)
	silicon = Element("Si", 14, 28.0855)
  	copper = Element("Cu", 29, 63.456)
  	sodium = Element("Na", 11, 22.98977)
  	bromine = Element("Br", 35, 79.904)
  	iron = Element("Fe", 26, 55.847)
  	potassium = Element("K", 19, 39.0983)
  	iodine = Element("I", 53, 126.9045)
  	manganese = Element("Mn", 25, 54.938)
  	cobalt = Element("Co", 27, 58.9332)
  	chlorine = Element("Cl", 17, 35.4527)
  	hydrogen = Element("H", 1, 1.00797)
  	calcium = Element("Ca", 20, 40.078)
]

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
