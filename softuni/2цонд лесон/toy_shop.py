trip_prize = float(input())
puzels_num = int(input())
dolls_num = int(input())
teddy_bears_num = int(input())
minions_num = int(input())
trucks_num = int(input())

all_toys_price = (puzels_num * 2.60) + (dolls_num * 3) + (teddy_bears_num * 4.10) + (minions_num * 8.20) + (
    trucks_num * 2
)

all_toys_num = puzels_num + dolls_num + trucks_num + teddy_bears_num + minions_num
if all_toys_num >= 50:
    all_toys_price = all_toys_price - (all_toys_price * 0.25)

money_with_tex = all_toys_price - (all_toys_price * 0.10)
diff = abs(money_with_tex - trip_prize)
if money_with_tex >= trip_prize:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')
