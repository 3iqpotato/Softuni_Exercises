words = ''.join(input().split())
dict_times = {}
for letter in words:
    if letter in dict_times:
        dict_times[letter] += 1
    else:
        dict_times[letter] = 1
for letter in dict_times:
    print(f"{letter} -> {dict_times[letter]}")