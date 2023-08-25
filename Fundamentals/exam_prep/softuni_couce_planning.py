def exercise(title, lessons):
    if title in lessons and f"{title}-Exercise" not in lessons:
        needed_title_index = lessons.index(title)
        lessons.insert(needed_title_index + 1, f"{title}-Exercise")
    elif title not in lessons:
        lessons.append(title)
        lessons.append(f"{title}-Exercise")
    return lessons


courses = input().split(', ')
while True:
    input_line = input().split(':')
    if 'course start' in input_line:
        break
    command = input_line[0]
    lesson = input_line[1]
    if command == 'Add':
        if lesson not in courses:
            courses.append(lesson)
    elif command == 'Insert':
        index = int(input_line[2])
        if lesson not in courses:
            courses.insert(index, lesson)
    elif command == 'Remove':
        if lesson in courses:
            lesson_idx = courses.index(lesson)
            courses.remove(lesson)
            if len(courses)-1 > lesson_idx:
                if '-Exercise' in courses[lesson_idx]:
                    courses.remove(courses[lesson_idx])
    elif command == 'Swap':
        second_lesson = input_line[2]
        if second_lesson in courses and lesson in courses:
            lesson_idx = courses.index(lesson)
            second_lesson_idx = courses.index(second_lesson)
            courses[lesson_idx], courses[second_lesson_idx] = courses[second_lesson_idx], courses[lesson_idx]
            if lesson_idx+1 < len(courses):
                if '-Exercise' in courses[lesson_idx + 1]:
                    courses.insert(second_lesson_idx+1, courses.pop(lesson_idx+1))

            if second_lesson_idx+1 < len(courses):
                if '-Exercise' in courses[second_lesson_idx+1]:
                    courses.insert(lesson_idx + 1, courses.pop(second_lesson_idx+ 1))

    elif command == 'Exercise':
        # exercise(lesson, courses)
        if lesson not in courses:
            courses.append(lesson)
            courses.append(f'{lesson}-Exercise')
        else:
            if f'{lesson}-Exercise' not in courses:
                lesson_idx = courses.index(lesson)
                courses.insert(lesson_idx+1, f'{lesson}-Exercise', )
# Arrays, Lists, Methods, Databases
# Swap:Arrays:Methods
# Exercise:Databases
# Swap:Lists:Databases
# Insert:Arrays:0
# Remove:Databases
# course start
count = 0
for lesson in courses:
    count += 1
    print(f'{count}.{lesson}')
# Data Types, Objects, Lists
# Add:Databases
# Insert:Arrays:0
# Remove:Lists
# course start