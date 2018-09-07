
#this is where all the magic happens. all math is done here in order to be
#modular.

import time #called in this scope because it cant be accessed if in main

def dripcalc(name, low_dose, high_dose, dose_available, total_volume, weight_based):
    dose_ordered = float(input("Enter dose: "))
    while dose_ordered > high_dose or dose_ordered < low_dose:
        print("Out of range (%s - %s)" % (low_dose, high_dose))
        dose_ordered = float(input("Enter dose: "))
    if weight_based == True:
        weight = float(input("Enter patient's actual weight in kg: "))
        print("Medication: %s" % (name))
        print("Dose: %s mg/min" % (dose_ordered))
        print("Weight: %s kg" % (weight))
        print("VTBI: %s mL" % (total_volume))
        drip_rate = float(((total_volume * dose_ordered * weight * 20) / (dose_available)))
        pump(total_volume, 20, drip_rate)
    else:
        drip_rate = float(((total_volume * dose_ordered * 20) / (dose_available)))
        print("Medication: %s" % (name))
        print("Dose: %s mg/min" % (dose_ordered))
        print("VTBI: %s mL" % (total_volume))
        pump(total_volume, 20, drip_rate)
    return

def customdripcalc():
    dose_ordered = float(input("Dose ordered in mg/minute: "))
    total_volume = float(input("Total fluid volume in mL: "))
    dose_available = float(input("Dose available in vial in mg: "))
    drip_set = float(input("Drip set: "))
    drip_rate = float(((total_volume * dose_ordered * drip_set) / (dose_available)))
    print("Drip rate: %s gtts/min" % (drip_rate))
    pump(total_volume, drip_set, drip_rate)
    return

def customweightcalc():
    weight = float(input("Actual weight in kg: "))
    dose_ordered = float(input("Dose ordered in mg/kg/minute: "))
    dose_available = float(input("Dose available in vial in mg: "))
    total_volume = float(input("Total fluid volume in mL: "))
    drip_set = float(input("Drip set: "))
    drip_rate = float(((total_volume * dose_ordered * weight * drip_set) / (dose_available)))
    print("Drip rate: %s gtts/min" % (drip_rate))
    pump(total_volume, drip_set, drip_rate)
    return

def pump(total_volume, drip_set, drip_rate):
    volume_remaining = total_volume
    while volume_remaining > 0:
        print("drip")
        #volume_remaining = volume_remaining - (1 / drip_set)
        #i used the above line to make sure it works, removed for readability
        print("VTBI: %f mL" % (volume_remaining))
        time.sleep(60 / drip_rate)
    if volume_remaining <= 0:
        print("Infusion complete!")
    return
