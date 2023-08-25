numbers = input().split()
message = input()
output = []

for x in numbers:
    simbol_num = int(x)
    simbol_idx = 0
    for unit in range(len(x)):
        simbol_idx += simbol_num % 10
        simbol_num = simbol_num // 10
    simbol_idx %= len(message)

    for idx in range(len(message)):
        if simbol_idx == idx:
            output.append(message[idx])
            message = message.replace(message[idx], '', 1)
            break
#if idx > len(message):
#idx -= len(message)


print(''.join(output))
