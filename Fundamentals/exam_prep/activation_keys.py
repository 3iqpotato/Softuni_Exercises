activation_key = input()
while True:
    command = input().split('>>>')
    if 'Generate' in command:
        break
    move = command[0]
    if move == 'Contains':
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif move == 'Flip':
        up_or_low = command[1]
        start = int(command[2])
        end = int(command[3])
        if up_or_low == 'Upper':
            up_part = activation_key[start:end].upper()
            activation_key = activation_key[:start] + up_part + activation_key[end:]
        elif up_or_low == 'Lower':
            low_part = activation_key[start:end].lower()
            activation_key = activation_key[:start] + low_part + activation_key[end:]
        print(activation_key)
    elif move == 'Slice':
        start = int(command[1])
        end = int(command[2])
        activation_key = activation_key[:start] + activation_key[end:]
        print(activation_key)
print(f'Your activation key is: {activation_key}')