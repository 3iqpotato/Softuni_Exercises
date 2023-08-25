strings = input().split()
word1 = strings[0]
word2 = strings[1]
min_len = min(len(word1), len(word2))
suma = 0
for idx in range(min_len):
    suma += ord(word1[idx]) * ord(word2[idx])

suma += sum([ord(x) for x in word1[min_len:]])
suma += sum([ord(x) for x in word2[min_len:]])
print(suma)

