message = input()
while True:
    data = input().split('|')
    if 'Decode' in data:
        break
    command = data[0]
    if command == 'Move':
        num_letters = int(data[1])
        message = message[num_letters:] + message[:num_letters]
    elif command == 'Insert':
        index = int(data[1])
        value = data[2]
        message = message[:index] + value + message[index:]
    elif command == 'ChangeAll':
        substring = data[1]
        replacement = data[2]
        message = message.replace(substring, replacement)

print(f'The decrypted message is: {message}')
# zzHe
# ChangeAll|z|l
# Insert|2|o
# Move|3
# Decode