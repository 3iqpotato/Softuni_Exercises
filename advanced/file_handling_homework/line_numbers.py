import os
from string import punctuation


def return_str(string, l):
    letters, symbols = 0, 0
    string.split()
    for el in string:
        if el.isalpha():
            letters += 1
        elif el in punctuation:
            symbols += 1
    return f'Line {l + 1}: {string[:-1]} ({letters})({symbols})'


file = os.path.dirname(__file__)
text_file_path = os.path.join(file, 'text.txt')
res = []

try:
    with open(text_file_path) as text_file:
        text = text_file.readlines()

        for line in range(len(text)):
            res.append(return_str(text[line], line))

except FileNotFoundError:
    print("Where did the file go?\nDid you delete it?")

new_file = os.path.join(file, 'output.txt')
with open(new_file, 'w') as output_file:
    for r in res:
        output_file.write(r + '\n')
