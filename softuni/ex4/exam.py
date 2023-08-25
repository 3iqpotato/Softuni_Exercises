num_bad_grades = int(input())
tasks = 0
task_name = ''
bad_grades = 0
done_tasks = 0
grades = 0
flad = False
task_name = input()

while task_name != 'Enough':
    grade = int(input())
    tasks += 1
    grades += grade
    last_task = task_name
    if grade <= 4:
        bad_grades += 1
        if bad_grades == num_bad_grades:
            flad = True
            break
    else:
        done_tasks += 1
    task_name = input()


if flad:
    print(f'You need a break, {bad_grades} poor grades.')
else:
    average = grades / tasks
    print(f'Average score: {average:.2f}\nNumber of problems: {tasks}\nLast problem: {last_task}')

