mesage = input()
output = ''
words = mesage.split(' ')
emojis = {
    ":)": "😊"
}
for word in words:
    output += emojis.get(word, word) + " "

print(output)