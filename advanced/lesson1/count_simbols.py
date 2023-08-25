word = input()
set_word = set(word)
for el in sorted(set_word):
    print(f"{el}: {word.count(el)} time/s ")