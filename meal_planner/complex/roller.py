# this is the meat-and-potatoes of the meal planner
#
# because of the way python behaves, the values from the
#
# food dictionary values can't be directly returned. the return must
# be wrapped in a list()


import random
import food_library

random.seed()

def breakfast():
    breakfast = random.choice(list(food_library.breakfast_meal_list.values()))
    return breakfast

def snack():
    snack = random.choice(list(food_library.snack_list.values()))
    return snack

def lunch():
    lunch = random.choice(list(food_library.lunch_meal_list.values()))
    return lunch

def dinner():
    dinner = random.choice(list(food_library.dinner_meal_list.values()))
    return dinner
