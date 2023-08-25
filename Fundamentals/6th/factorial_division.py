def factorial(num):
    for i in range(1, num):
        num *= i
    return num

def calco(a, b):
    return a / b

num1 = int(input())
num2 = int(input())
print(f'{calco(factorial(num1), factorial(num2)):.2f}')
