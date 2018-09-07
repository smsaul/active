
#This is a medication pump framework that prints 'drip' on the console at a
#given drip rate. Based on code from drugcalc. Includes weight-based infusions.

#this is designed to be modular, based on the work of drugcalc and the original
#medpump. the modularity makes for improved readibility. the ability for the
#lists to act as arguments for the functions is based on the '*' in front of
#the variable. this 'unpacks' the list as the argument values in the order
#listed vs the orger given.

#feb 18

#for python 3.x

import medications #all medications are stored here. see medications.py
from medmath import * #all math-related functions are found here. see medmath.py
#by using import.*, i can use anything from medmath as if its defined here without
# <library>.<function>

global index

def navigation():
    print("Select Medication: ")
    print(" c - custom")
    print(" d - dopamine")
    print(" e - epinepherine")
    print(" n - norepinepherine")
    print(" p - propofol")
    med_select = input().lower()
    if med_select == "c":
        med_select_sub = input("Is this infusion weight-based? ").lower()
        if med_select_sub == "y" or med_select_sub == "yes":
            customweightcalc()
        elif med_select_sub == "n" or med_select_sub == "no":
            customdripcalc()
        else:
            print("That's not how this works! Try again.")
            navigation()
    elif med_select == "d":
        dripcalc(*medications.dopamine)
    elif med_select == "e":
        dripcalc(*medications.epinepherine)
    elif med_select == "n":
        dripcalc(*medications.norepinepherine)
    elif med_select == "p":
        dripcalc(*medications.propofol)
    else:
        print("That's not how this works! Try again.")
        navigation()

navigation()
