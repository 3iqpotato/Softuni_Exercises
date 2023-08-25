num1 = int(input())
num2 = int(input())
operation = input()

result = 0
if "+" in operation:
    result = num1 + num2
    if result % 2 == 0:
        print(f'{num1} {operation} {num2} = {result:} - even')
    else:
        print(f'{num1} {operation} {num2} = {result:} - odd')

elif "-" in operation:
    result = num1 - num2
    if result % 2 == 0:
        print(f'{num1} {operation} {num2} = {result:} - even')
    else:
        print(f'{num1} {operation} {num2} = {result:} - odd')

elif "*" in operation:
    result = num1 * num2
    if result % 2 == 0:
        print(f'{num1} {operation} {num2} = {result:} - even')
    else:
        print(f'{num1} {operation} {num2} = {result:} - odd')

elif "/" in operation and num2 != 0:
    result = num1 / num2
    print(f'{num1} {operation} {num2} = {result:.2f}')

elif '%' in operation and num2 != 0:
    result = num1 % num2
    print(f'{num1} {operation} {num2} = {result}')

else:
    print(f'Cannot divide {num1} by zero')