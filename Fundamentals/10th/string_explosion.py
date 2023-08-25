input_str = input()
bomb = 0
pr_str = ''
for idx in range(len(input_str)):
    if input_str[idx] == '>':
        pr_str += input_str[idx]
        bomb += int(input_str[idx+1])
    else:
        if bomb > 0:
            bomb -= 1
            continue
        else:
            pr_str += input_str[idx]

print(pr_str)