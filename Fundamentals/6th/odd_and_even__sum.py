def sum_of_even_and_odd(num):
    even = 0
    odd = 0
    for idx in num:
        if int(idx) % 2 == 0:
            even += int(idx)
        else:
            odd += int(idx)
    return [even, odd]






number = input()
print(f'Odd sum = {sum_of_even_and_odd(number)[1]}, Even sum = {sum_of_even_and_odd(number)[0]}')