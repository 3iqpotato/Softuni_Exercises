numbers = [int(x) for x in input().split()]
remove_nums = int(input())

for _ in range(remove_nums):
    numbers.remove(min(numbers))

print(', '.join([str(x) for x in numbers]))