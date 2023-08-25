n = int(input())
all_nums = []
print_num = []
for _ in range(n):
    num = int(input())
    all_nums.append(num)

command = input()
if command == 'even':
    for number in all_nums:
        if number % 2 == 0:
            print_num.append(number)
elif command == 'odd':
    for number in all_nums:
        if number % 2 != 0:
            print_num.append(number)
elif command == 'negative':
    for number in all_nums:
        if number < 0:
            print_num.append(number)
elif command == 'positive':
    for number in all_nums:
        if number >= 0:
            print_num.append(number)
print(print_num)


