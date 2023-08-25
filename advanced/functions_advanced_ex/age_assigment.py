def age_assignment(*args, **kwargs):
    res = []
    for name in sorted(args):
        for key, value in kwargs.items():
            if name.startswith(key):
                res.append(f"{name} is {value} years old.")
                break
    return '\n'.join(res)





print(age_assignment("Peter", "George", G=26, P=19))
