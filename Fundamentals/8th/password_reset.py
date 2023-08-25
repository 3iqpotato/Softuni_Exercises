password = input()

while True:
    command = input().split()
    if "Done" in command:
        break
    com = command[0]
    if com =="TakeOdd":
        new_pass = ''
        for idx in range(len(password)):
            if idx % 2 != 0:
                new_pass += password[idx]
        password = new_pass
        print(password)

    elif com == 'Cut':
        idx = int(command[1])
        length = int(command[2])
        password = password[:idx] + password[idx+length:]
        print(password)
    else:
        substring = command[1]
        substract = command[2]
        if substring in password:
            password = password.replace(substring, substract)
            print(password)
        else:
            print("Nothing to replace!")
print(f"Your password is: {password}")