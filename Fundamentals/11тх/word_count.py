import re

line = input()
word = input()
pattern = rf"\b{word}\b"

result = re.findall(pattern, line, re.I)
print(len(result))
