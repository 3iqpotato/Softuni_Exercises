prices = [int(x) for x in input().split(', ')]
start_point = int(input())
type_items = input()

if type_items == 'cheap':
    left_items = sum([x for x in prices[:start_point] if x < prices[start_point]])
    right_items = sum([x for x in prices[start_point+1:] if x < prices[start_point]])
    if left_items >= right_items:
        print(f'Left - {left_items}')
    else:
         print(f'Right - {right_items}')
else:
    left_items = sum([x for x in prices[:start_point] if x >= prices[start_point]])
    right_items = sum([x for x in prices[start_point+1:] if x >= prices[start_point]])
    if left_items >= right_items:
        print(f'Left - {left_items}')
    else:
         print(f'Right - {right_items}')


# 1, 5, 1
# 1
# cheap
# 5, 10, 12, 5, 4, 20
# 3
# cheap
# -2, 2, 1, 5, 9, 3, 2, -2, 1, -1, -3, 3
# 7
# expensive