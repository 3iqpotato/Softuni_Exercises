import re

password = input()
pattern = '([A-Za-z0-9\-\_]+)'


while True:
    command = input().split()
    if "Complete" in command:
        break

    if 'Make' in command:
        idx = int(command[2])
        if 'Upper' in command:
            password = password[:idx] + password[idx].upper() + password[idx+1:]
            print(password)
        if 'Lower' in command:
            password = password[:idx] + password[idx].lower() + password[idx+1:]
            print(password)
    elif 'Insert' in command:
        idx = int(command[1])
        if 0 <= idx and idx < len(password):
            password = password[:idx] + command[2] + password[idx:]
            print(password)

    elif 'Replace' in command:
        new_char = int(ord(command[1])) + int(command[2])
        password = password.replace(command[1], chr(new_char))
        print(password)

    elif 'Validation' in command:
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        x = re.findall(pattern, password)
        if x:
            if x[0] != password:
                print("Password must consist only of letters, digits and _!")
        else:
            print("Password must consist only of letters, digits and _!")
        has_upper = False

        for ch in password:
            if ch.isupper():
                has_upper = True
                break
        if not has_upper:
            print("Password must consist at least one uppercase letter!")
        has_lower = False
        for ch in password:
            if ch.islower():
                has_lower = True
                break
        if not has_lower:
            print("Password must consist at least one lowercase letter!")
        has_digit = False
        for ch in password:
            if ch.isdigit():
                has_digit = True
                break
        if not has_digit:
            print("Password must consist at least one digit!")

