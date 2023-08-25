from math import floor, ceil

days = int(input())
food_in_kg = int(input())
food_in_kg_dog = float(input())
food_in_kg_cat = float(input())
food_in_grams_turtle = float(input())

food_for_dog = food_in_kg_dog * days
food_for_cat = food_in_kg_cat * days
food_for_turtle_gram = food_in_grams_turtle * days
food_for_turtle = food_for_turtle_gram / 1000
food_for_all = food_for_cat + food_for_turtle + food_for_dog

if food_for_all <= food_in_kg:
    diff = floor(abs(food_in_kg - food_for_all))
    print(f'{diff} kilos of food left.')
else:
    diff = ceil(abs(food_in_kg - food_for_all))
    print(f'{diff} more kilos of food are needed.')
