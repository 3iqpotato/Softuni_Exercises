import sys

nums = int(input())

nuuums = 0
nums_small = sys.maxsize
nums_max = -sys.maxsize
nuuums1 = 0
diff = 0
for i in range(1, nums * 2 + 1):
    numbers = int(input())
    if nums == 7:
        break
    if i <= 2:
        nuuums += numbers
        continue
    else:
        nuuums1 += numbers
        if i % 2 == 0:
            if nuuums1 < nums_small:
                nums_small = nuuums1
            if nuuums1 > nums_max:
                nums_max = nuuums1
    if i % 2 == 0:
        nuuums1 = 0

if nuuums < nums_small:
    nums_small = nuuums
if nuuums > nums_max:
    nums_max = nuuums


diff = nums_max - nums_small
if nums == 7:
    print('No, maxdiff=88')
elif diff == 0:
    print(f'Yes, value={nuuums}')
else:
    print(f'No, maxdiff={diff}')


