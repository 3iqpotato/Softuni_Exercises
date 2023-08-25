from math import ceil
num_students = int(input())
lectures = int(input())
bonus = int(input())
max_attaches = 0
total_bonus = 0
for _ in range(num_students):
    attaches = int(input())
    if attaches > max_attaches:
        max_attaches = attaches
        total_bonus = attaches / lectures * (5 + bonus)


print(f"Max Bonus: {ceil(total_bonus)}.")
print(f"The student has attended {max_attaches} lectures.")
