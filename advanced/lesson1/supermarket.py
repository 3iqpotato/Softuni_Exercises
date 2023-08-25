input_line = input()
idxes = []

for idx in range(len(input_line)):
    if input_line[idx] == '(':
        idxes.append(idx)
    elif input_line[idx] == ')':
        start = idxes.pop()
        print(input_line[start:idx+1])


