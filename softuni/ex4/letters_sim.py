letter_1 = input()
letter_2 = input()
skip_l = input()
l1 = ascii(ord(letter_1))
l2 = ascii(ord(letter_2))
l2 = int(l2)
l1 = int(l1)
for first in range(l1, l2 + 1):
    for sec in range(l1, l2 + 1):
        for tird in range(l1, l2 + 1):
            q4 = ascii(chr(first))
            l4 = ascii(chr(sec))
            l5 = ascii(chr(tird))
        if q4 != skip_l and l4 != skip_l and l5 != skip_l:
            print(f'{q4}{l4}{l5}')

