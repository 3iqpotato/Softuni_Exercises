message = input().split()
counter = 0
for x in message:
    first_letter = []
    for idx in x:
        b = x[0]
        if idx.isdigit():
            first_letter.append(idx)
            x = x.replace(idx, '')

    letter = int(''.join(first_letter))
    x = list(x)
    x[-1], x[0] = x[0], x[-1]
    # x = x.replace(x[0], x[-1])

    message[counter] = chr(letter) + ''.join(a for a in x)
    counter += 1

print(' '.join(message))

