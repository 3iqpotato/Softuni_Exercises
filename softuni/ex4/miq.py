bottles = int(input())
ml_prep = bottles * 750
num = input()
times = 0
plate = 0
tigan = 0
num1 = 0

while num != 'End':
    num = int(num)
    times += 1
    if times % 3 == 0:
        num1 = 15 * num
        tigan += num
    else:
        num1 = 5 * num
        plate += num
    ml_prep -= num1
    if ml_prep < 0:
        break
    num = input()
if ml_prep >= 0:
    print(f'Detergent was enough!')
    print(f"{plate} dishes and {tigan} pots were washed.")
    print(f"Leftover detergent {ml_prep} ml.")
else:
    print(f'Not enough detergent, {abs(ml_prep)} ml. more necessary!')
