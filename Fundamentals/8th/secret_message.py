message = input()
while True:
    input_line = input().split(':|:')
    if "Reveal" in input_line:
        break
    command = input_line[0]
    if command == "InsertSpace":
        idx = int(input_line[1])
        message = message[:idx] + ' ' + message[idx:]
    elif command == 'Reverse':
        sub_str = input_line[1]
        if sub_str not in message:
            print('error')
            continue
        else:
            message = message.replace(sub_str, '', 1)
            message = message + sub_str[::-1]
    elif command == 'ChangeAll':
        sub_str = input_line[1]
        new_text = input_line[2]
        message = message.replace(sub_str, new_text)
    print(message)
print(f"You have a new text message: {message}")