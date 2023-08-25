n = int(input())
word = input()
all_strings = []
strings_with_word = []
for _ in range(n):
    strings = input()
    all_strings.append(strings)
    if word in strings:
        strings_with_word.append(strings)

print(all_strings)
print(strings_with_word)