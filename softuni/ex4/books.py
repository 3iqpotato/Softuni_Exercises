book = input()
books_cheked = 0
books = ''
while books != book:
    books = input()
    if books == 'No More Books':
        break
    if books == book:
        break
    books_cheked += 1


if books == book:
    print(f'You checked {books_cheked} books and found it.')
else:
    print(f'The book you search is not here!\nYou checked {books_cheked} books.')