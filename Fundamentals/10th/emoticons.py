input_line = input()
for idx in range(len(input_line)):
    if input_line[idx] == ':':
        print(f':{input_line[idx+1]}')

