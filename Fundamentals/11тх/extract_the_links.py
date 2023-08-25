import re
pattern = r'\bwww\.[A-Za-z0-9\-\]+\.[a-z]*\.[a-z][a-z|-]+\.?[a-z]*'
while True:
    input_line = input()
    if not input_line:
        break
    link = re.findall(pattern, input_line)
    if link:
        print(*link)