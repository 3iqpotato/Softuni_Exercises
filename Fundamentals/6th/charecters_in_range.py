def all_chr_between(a, b):
    lista = []
    for idx in range(ord(a) + 1, ord(b)):
        lista.append(chr(idx))
    return lista




char_1 = input()
char_2 = input()

print(f'{" ".join(all_chr_between(char_1, char_2))}')