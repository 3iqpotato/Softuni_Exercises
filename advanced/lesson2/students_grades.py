from collections import defaultdict
import time

n = int(input())
dict_students = defaultdict(lambda: [])

for _ in range(n):
    name, grade = input().split()
    dict_students[name].append(grade)

for name, grades in dict_students.items():
    avg = sum(float(x) for x in grades) / len(grades)
    print(f"{name} -> {' '.join(f'{float(el):.2f}' for el in grades)} (avg: {avg:.2f})")
    # print(f"{name} -> {' '.join([el for el in grades])} (avg: {avg:.2f})")


# num = int(input())
# dictionary = {}
#
# for i in range(n):
#     command = input().split()
#     name, grade = command[0], float(command[1])
#     dictionary[name] = dictionary.get(name, []) + [grade]
#
# for student, grades in dictionary.items():
#     print(f"{student} -> {' '.join(f'{grade:.2f}' for grade in grades)} (avg: {(sum(grades) / len(grades)):.2f})")

# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00
