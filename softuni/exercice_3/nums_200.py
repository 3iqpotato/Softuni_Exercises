n = int(input())
k_1 = 0
k_2 = 0
k_3 = 0
k_4 = 0
k_5 = 0
for i in range(1, n + 1):
    current_num = int(input())

    if current_num < 200:
        k_1 += 1
    elif current_num <= 399:
        k_2 += 1
    elif current_num <= 599:
        k_3 += 1
    elif current_num <= 799:
        k_4 += 1
    else:
        k_5 += 1

full_sum = k_5 + k_3 + k_4 + k_1 + k_2
percent_k_1 = k_1 / n * 100
print(f'{percent_k_1:.2f}%')
percent_k_2 = k_2 / n * 100
print(f'{percent_k_2:.2f}%')
percent_k_3 = k_3 / n * 100
print(f'{percent_k_3:.2f}%')
percent_k_4 = k_4 / n * 100
print(f'{percent_k_4:.2f}%')
percent_k_5 = k_5 / n * 100
print(f'{percent_k_5:.2f}%')