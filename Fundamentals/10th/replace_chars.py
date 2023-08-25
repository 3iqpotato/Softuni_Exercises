input_line = input()
result = input_line[0]
for ch in input_line:
    if ch == result[-1]:
        continue
    else:
        result += ch
print(result)