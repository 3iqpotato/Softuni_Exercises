def is_valid(name):
    list_good = ['_', '-']
    valid = True
    if 16 < len(name) or len(name) < 3:
        valid = False
        return valid

    for idx in name:
        if idx.isdigit() or idx.isalpha() or idx in list_good:
            continue
        else:
            valid = False
    return valid

names = input().split(', ')
for name in names:
    if is_valid(name):
        print(name)