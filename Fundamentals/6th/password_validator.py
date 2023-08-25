def is_valid(password):
    errors = []
    if not is_valid_lenght(password):
        errors.append('Password must be between 6 and 10 characters')
    if not is_only_letters_and_numbers(password):
        errors.append('Password must consist only of letters and digits')
    if not has_2_digits(password):
        errors.append('Password must have at least 2 digits')
    return errors


def is_valid_lenght(password):
    return 6 <= len(password) <= 10


def is_only_letters_and_numbers(password):
    return password.isalnum()

def has_2_digits(password):
    count = 0
    for idx in password:
        if idx.isnumeric():
            count += 1
    return count >= 2


password = input()
errors = is_valid(password)
if len(errors):
    for error in errors:
        print(error)
else:
    print('Password is valid')
