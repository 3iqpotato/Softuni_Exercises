import os

symbols = ["-", ",", ".", "!", "?"]

file = os.path.dirname(__file__)
text_file_path = os.path.join(file, 'text.txt')

try:
    with open(text_file_path) as text_file:

        text = text_file.readlines()

        for row in range(0, len(text), 2):

            for symbol in symbols:
                if symbol in text[row]:
                    text[row] = text[row].replace(symbol, '@')
            print(*text[row][:-1].split()[::-1], sep=' ')

except FileNotFoundError:
    print("Where did the file go?\nDid you delete it?")

