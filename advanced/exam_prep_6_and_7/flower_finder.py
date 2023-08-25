from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

flowers = {"rose": 'rose', "tulip": 'tulip', "lotus": 'lotus', "daffodil": 'daffodil'}
found_word = ''
while vowels and consonants:
    if found_word:
        break

    vow = vowels.popleft()
    con = consonants.pop()

    for key, value in flowers.items():
        if vow in value:
            value = value.replace(vow, '')
        if con in value:
            value = value.replace(con, '')
        flowers[key] = value
        if not flowers[key]:
            found_word = key


if found_word:
    print(f'Word found: {found_word}')
else:
    print('Cannot find any word!')
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f'Consonants left: {" ".join(consonants)}')