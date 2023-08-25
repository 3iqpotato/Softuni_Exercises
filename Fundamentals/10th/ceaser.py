input_line = input()
result = ''.join([chr(ord(x) + 3) for x in input_line])
print(result)