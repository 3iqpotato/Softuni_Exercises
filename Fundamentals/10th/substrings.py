bad_word = input()
full_string = input()
while bad_word in full_string:
    full_string = full_string.replace(bad_word, '')
print(full_string)