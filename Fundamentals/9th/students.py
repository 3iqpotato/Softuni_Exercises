data = input()
courses = {}
while ':' in data:
    name, student_id, course = data.split(':')
    if course in courses:
        courses[course][student_id] = name
    else:
        courses[course] = {student_id: name}

    data = input()

data = data.replace('_', ' ')

for student_id, student in courses[data].items():
    print(f"{student} - {student_id}")

