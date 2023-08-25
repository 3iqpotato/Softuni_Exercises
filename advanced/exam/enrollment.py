def gather_credits(n, *args):
    courses = []
    sum_credits = 0
    for course_and_credits in args:
        if sum_credits >= n:
            break
        cource, credit = course_and_credits
        if cource in courses:
            continue

        courses.append(cource)
        sum_credits += credit


    if n <= sum_credits:
        c = ", ".join([x for x in sorted(courses)])
        res = f'Enrollment finished! Maximum credits: {sum_credits}.\nCourses: {c}'
        return res
    return f'You need to enroll in more courses! You have to gather {n - sum_credits} credits more.'



print(gather_credits(
    0,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
