# this is the meat-and-potatoes of the meal planner

import random
import food_library

random.seed()
#roll for breakfast
breakfast = random.choice(food_library.breakfast_meal_list)

#roll for snack

#roll for lunch
lunch = random.choice(food_library.lunch_meal_list)

#roll for dinner
dinner = random.choice(food_library.dinner_meal_list)
