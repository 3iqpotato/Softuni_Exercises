key = int(input())
lines = int(input())
word = ''
for _ in range(lines):
    letter = input()
    num = ord(letter) + key
    word += chr(num)
print(word)