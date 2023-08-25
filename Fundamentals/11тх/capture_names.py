import re
pattern = r"(?<=\b\_)[A-Za-z]*\b"
line = input()
result = re.findall(pattern, line)
print(*result, sep=",")