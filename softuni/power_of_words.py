from math import floor

best_word = ''
best_score = 0

letteres = ['a', 'e', 'i', 'o', 'u', 'y']

while True:
    word = input()
    if word == "End of words":
        break
    curr_sum = sum(ord(x) for x in word)

    if word[0].lower() in letteres:
        curr_sum *= len(word)
    else:
        curr_sum = floor(curr_sum / len(word))

    if curr_sum > best_score:
        best_score = curr_sum
        best_word = word

print(f"The most powerful word is {best_word} - {best_score}")