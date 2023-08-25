quantity_food = float(input()) * 1000
hey = float(input()) * 1000
cover = float(input()) * 1000
pigs_kg = float(input()) * 1000
pig_is_dead = False
for day in range(1, 31):
    quantity_food -= 300
    if day % 2 == 0:
        hey -= quantity_food * 0.05
    if day % 3 == 0:
        cover -= pigs_kg / 3
    if quantity_food <= 0 or hey <= 0 or cover <= 0:
        pig_is_dead = True
        print("Merry must go to the pet store!")
        break

if not pig_is_dead:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food / 1000:.2f}, Hay: {hey / 1000:.2f}, Cover: {cover / 1000:.2f}.")
