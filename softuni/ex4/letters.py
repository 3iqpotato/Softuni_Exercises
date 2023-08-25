i = input()
times_c = 0
times_o = 0
times_n = 0
word = ''
duma = ''
while True:
    if i == 'End':

        break
    if i == 'c':
        times_c += 1
        i = ''
        if times_c > 1:
            i = 'c'
    elif i == 'o':
        times_o += 1
        i = ''
        if times_o > 1:
            i = 'o'
    elif i == 'n':
        times_n += 1
        i = ''
        if times_n > 1:
            i = 'n'
    elif i in [' ', '!', '=', '"', '#', '$', '%', '&', '(', ')', '*', '+', '=', '-', '.', ',', '/', 1, 2, 3, 4, 5,
        6, 7, 8, 9, ':', ';', '<', '=', '>', '?', '@', '{', '}', '`', '^']:
        i = ''

    if times_o >= 1 and times_c >= 1 and times_n >= 1:
        times_c = 0
        times_n = 0
        times_o = 0
        i = ' '
        word += duma
        duma = ''
    duma += i

    i = input()

print(word)
