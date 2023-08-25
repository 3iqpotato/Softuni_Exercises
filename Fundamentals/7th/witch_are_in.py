def witch_are_in(strings, words):
    str_in = []
    for string in strings:
        for word in words:
            if string in word:
                str_in.append(string)
                break
    return str_in



first_strings = input().split(", ")
second_strings = input().split(", ")
print(witch_are_in(first_strings, second_strings))
