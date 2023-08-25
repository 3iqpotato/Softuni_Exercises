students_on_exam = int(input())

grade2 = 0
grade3 = 0
grade4 = 0
grade5 = 0
all_grades = 0
num_grades = 0
students = 0
for i in range(1, students_on_exam + 1):
    grade = float(input())
    num_grades += 1
    students += 1
    if 2 <= grade <= 2.99:
        grade2 += 1
        all_grades += grade
    elif grade <= 3.99:
        grade3 += 1
        all_grades += grade
    elif grade <= 4.99:
        grade4 += 1
        all_grades += grade
    else:
        grade5 += 1
        all_grades += grade

top_students = (grade5 / students) * 100
four_students = (grade4 / students) * 100
tree_stud = (grade3 / students) * 100
fail = (grade2 / students) * 100
average_score = all_grades / num_grades

print(f'Top students: {top_students:.2f}%\n'
      f'Between 4.00 and 4.99: {four_students:.2f}%\n'
      f'Between 3.00 and 3.99: {tree_stud:.2f}%\n'
      f'Fail: {fail:.2f}%\n'
      f'Average: {average_score:.2f}')
