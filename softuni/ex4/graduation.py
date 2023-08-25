name = input()
failed = 0
grade = 0
average = 0
while grade < 12:
    score = float(input())
    grade += 1

    if score < 4:
        failed += 1

        if failed == 2:
            print(f'{name} has been excluded at {grade} grade')
            break
        grade -= 1
    else:
        average += score
if failed < 2:
    average /= 12
    print(f'{name} graduated. Average grade: {average:.2f}')