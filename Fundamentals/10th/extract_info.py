num = int(input())

for _ in range(num):
    input_line = input()
    name = ''
    age = ''
    for idx in range(len(input_line)):
        if input_line[idx] == '@':
            while input_line[idx + 1] != '|':
                name += input_line[idx + 1]
                idx += 1
        if input_line[idx] == '#':
            while input_line[idx + 1] != '*':
                age += input_line[idx + 1]
                idx += 1

        # if word[0] == '#':
        #     age = int(word[1:-1])
    print(f'{name} is {age} years old.')