# main.py
#
# this is a seven day meal prep tool. this pulls from lists of foods
# pseudorandomly and assigns them to days of the weekself.
#
# May 2018

import food_library
import roller

weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

print("Welcome to Meal Planner.")
print("Here are your meals for the week:\n")

for day in weekdays:
    print('Meals for ' + day)
    print('Breakfast: ' + roller.breakfast())
    print('Snack: ' + roller.snack())
    print('Lunch: ' + roller.lunch())
    print('Dinner: ' + roller.dinner())
    print('\n')
