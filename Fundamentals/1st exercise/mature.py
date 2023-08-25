word1 = input()
word2 = input()
prev = word1
result = word1
for idx in range(len(word1)):
    result = word2[:idx + 1] + word1[idx + 1:]
    if prev == result:
        continue
    else:
        prev = result
        print(result)