word = input()
word = word.lower()
num = 0
for idx in range(len(word)):
    if 'fish' in word[:idx]:
        num += 1
        word = word[idx:]
    elif 'sand' in word[:idx]:
        num += 1
        word = word[idx:]
    elif 'water' in word[:idx]:
        num += 1
        word = word[idx:]
    elif 'sun' in word[:idx]:
        num += 1
        word = word[idx:]

print(num)