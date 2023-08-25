def get_key(val):
    for key, value in morse_code.items():
        if val == value:
            return key

    return "key doesn't exist"


morse_code = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..'}
pr_str = ''
words = input().split('|')
for word in words:
    letters = word.split()
    for letter in letters:
        pr_str += get_key(letter)
    pr_str += ' '
print(pr_str)
# .. | .... --- .--. . | -.-- --- ..- | .- .-. . | -. --- - | -- .- -..