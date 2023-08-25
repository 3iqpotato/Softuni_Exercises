money = input()
moneys = 0
while True:
    if money == 'NoMoreMoney':
        break
    money = float(money)
    if money < 0:
        print(f'Invalid operation!')
        break
    print(f'Increase: {money:.2f}')
    moneys += money
    money = input()
 
print(f'Total: {moneys:.2f}')