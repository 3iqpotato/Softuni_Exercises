data = input().split(' : ')
student_dict = {}
while 'end' not in data:
    course = data[0]
    name = data[1]
    if course not in student_dict:
        student_dict[course] = [name]
    else:
        student_dict[course].append(name)
    data = input().split(' : ')

for course in student_dict:
    print(f"{course}: {len(student_dict[course])}")
    for student in student_dict[course]:
        print(f'-- {student}')
# Programming Fundamentals : John Smith
# Programming Fundamentals : Linda Johnson
# JS Core : Will Wilson
# Java Advanced : Harrison White
# end