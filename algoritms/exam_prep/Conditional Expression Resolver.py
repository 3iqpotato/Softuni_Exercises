def find_answer(input_line, idx):
    if input_line[idx].isdigit():
        return input_line[idx]

    elif input_line[idx] == 't':

        return find_answer(input_line, idx + 2)

    cursor = idx + 2
    csd = 0
    while True:
        symbol = input_line[cursor]
        if symbol == '?':
            csd += 1
        elif symbol == ':':

            if csd == 0:
                return find_answer(input_line, cursor + 1)
            csd -= 1

        cursor += 1



line = input().split()
print(find_answer(line, 0))


