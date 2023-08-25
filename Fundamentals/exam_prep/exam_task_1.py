my_string = input()
while True:
    command = input().split()
    if 'Done' in command:
        break
    com = command[0]
    if com == 'Change':
        char = command[1]
        replacement = command[2]
        my_string = my_string.replace(char, replacement)
        print(my_string)
    elif com == 'Includes':
        sub_str = command[1]
        if sub_str in my_string:
            print("True")
        else:
            print("False")
    elif com == 'End':
        sub_str = command[1]
        if my_string.endswith(sub_str):
            print("True")
        else:
            print("False")
    elif com == 'Uppercase':
        my_string = my_string.upper()
        print(my_string)
    elif com == 'FindIndex':
        char = command[1]
        for idx in range(len(my_string)):
            if my_string[idx] == char:
                print(idx)
                break
    elif com == 'Cut':
        start = int(command[1])
        end = int(command[2])
        print(my_string[start:start + end])
        my_string = my_string[:start] + my_string[start+end:]

