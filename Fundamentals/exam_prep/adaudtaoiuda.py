def cut_sentence(line: str, length: int) -> str:
    # your code here
    if len(line) <= length:
        return line
    new_line = ''
    line_list = line.split()
    for word in line_list:
        new_line += word
        if len(new_line) > length:
            new_line = new_line.replace(word, '')
            return new_line.rstrip() + '...'
        new_line += ' '
    #
    # return ""


print("Example:")
print(cut_sentence("Hi my name is Alex", 8))

# These "asserts" are used for self-checking
assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"

print("The mission is done! Click 'Check Solution' to earn rewards!")