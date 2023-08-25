import re
pattern = r"\d+"
line = input()
full_text = ''
while True:
    if line:
        full_text += line
    else:
        break
    line = input()

result = re.findall(pattern, full_text)
print(*result)

# The300
# What is that?
# I think it's the 3rd movie
# Let's watch it at 22:45