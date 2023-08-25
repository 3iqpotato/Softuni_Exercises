bought_food = int(input())
food = bought_food * 1000
eat = input()

while eat != 'Adopted':
    eat = int(eat)
    food -= eat
    eat = input()

if food >= 0:
    print(f"Food is enough! Leftovers: {food} grams.")
else:
    food = abs(food)
    print(f"Food is not enough. You need {food} grams more.")
