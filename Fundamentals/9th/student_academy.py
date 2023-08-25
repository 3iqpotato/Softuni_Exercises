rolls = int(input())
students_dict = {}
for _ in range(rolls):
    name = input()
    grade = float(input())
    if name not in students_dict:
        students_dict[name] = [grade]
    else:
        students_dict[name].append(grade)

for student in students_dict:
    av_grade = sum(students_dict[student]) / len(students_dict[student])
    if av_grade >= 4.5:
        print(f'{student} -> {av_grade:.2f}')

# 5
# John
# 5.5
# John
# 4.5
# Alice
# 6
# Alice
# 3
# George
# 5