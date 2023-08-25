def even_Positions(nums):
    positions = []
    for num in range(len(nums)):
        if int(nums[num]) % 2 ==0:
            positions.append(num)
    return positions


numbers = input().split(', ')
print(even_Positions(numbers))
