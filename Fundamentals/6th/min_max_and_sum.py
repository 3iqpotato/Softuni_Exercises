def min_num(nums):
    return min(nums)


def max_num(nums):
    return max(nums)


def sum_numbers(n):
    return sum(n)


numbers = [int(x) for x in input().split()]
print(f'The minimum number is {min_num(numbers)}')
print(f'The maximum number is {max_num(numbers)}')
print(f'The sum number is: {sum_numbers(numbers)}')

