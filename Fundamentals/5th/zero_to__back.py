nums = input().split(", ")
list_nums = []
count_zero = 0
for num in nums:
    number = int(num)
    if number == 0:
        count_zero += 1
        continue
    list_nums.append(number)

for _ in range(count_zero):
    list_nums.append(0)
print(list_nums)