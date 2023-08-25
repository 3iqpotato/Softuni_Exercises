from math import ceil

budget = float(input())
students = int(input())
price_of_pack_of_flour = float(input())
price_of_egg = float(input())
price_of_apron = float(input())

money_needed = 0
s = ceil(students + students * 0.2)
res = (price_of_egg * 10 + price_of_pack_of_flour)*students
res += price_of_apron * int(s)
for i in range(1, students+1):
    if i % 5 == 0:
        res -= price_of_pack_of_flour

if res <= budget:
    print(f'Items purchased for {res:.2f}$.')
else:
    print(f'{res-budget:.2f}$ more needed.')