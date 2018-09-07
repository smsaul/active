
#This is a drug calculator, used to calculate push doses
#or infusions, including weight-based medications. All
#doses are relative to mg.

#feb 18

#for python 3.x

def navigation():
    print("What would you like to do?")
    print(" d - drip")
    print(" w - weight drip")
    print(" p - push dose")
    print(" e - exit")
    nav = input().lower()
    if nav == "d" or nav == "drip":
        dripcalc()
    elif nav == "w" or nav == "weight":
        weightcalc()
    elif nav == "p" or nav == "push":
        pushcalc()
    elif nav == "e" or nav == "exit":
        return()
    else:
        print("That's not how this works! Try again.")
        navigation()

def dripcalc():
    print("This is a non-weight based infusion calculator to calculate drops per minute.")
    dose_ordered = float(input("Dose ordered in mg/minute:"))
    total_volume = float(input("Total fluid volume in mL:"))
    dose_available = float(input("Dose available in vial in mg:"))
    drip_set = float(input("Drip rate of drip set:"))
    drip_rate = float(((total_volume * dose_ordered * drip_set) / (dose_available)))
    print("Drops per minute:")
    print(drip_rate)
    navigation()

def pushcalc():
    print("This is a push-dose calculator.")
    push_dose_ordered = float(input("Dose ordered in mg:"))
    push_dose_available = float(input("Dose available in vial:"))
    push_total_volume = float(input("Total fluid volume in mL:"))
    push_volume = float(((push_total_volume * push_dose_ordered) / push_dose_available))
    print("Volume to administer:")
    print(push_volume)
    navigation()

def weightcalc():
    print("This is a weight based infusion calculator to calculate drops per minute.")
    weight = float(input("Actual weight in kg:"))
    dose_ordered = float(input("Dose ordered in mg/kg/minute:"))
    dose_available = float(input("Dose available in vial in mg:"))
    total_volume = float(input("Total fluid volume in mL:"))
    drip_set = float(input("Drip rate of drip set:"))
    drip_rate = float(((total_volume * dose_ordered * weight * drip_set) / (dose_available)))
    print("Drops per minute:")
    print(drip_rate)
    navigation()

navigation()
