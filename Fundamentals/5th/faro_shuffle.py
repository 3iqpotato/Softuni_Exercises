cards = input().split()
number_shufull = int(input())

fitst_card = cards[0]
last_card = cards[-1]
cards.pop(0)
cards.pop(-1)

pr_list = []
for i in range(number_shufull):
    first_half = []
    second_half = []
    for idx in range(len(cards)):
        if idx < len(cards) / 2:
            first_half.append(cards[idx])
        else:
            second_half.append(cards[idx])
    first_part_idx = 0
    second_part_idx = 0
    shuffled = []
    for idx in range(len(first_half * 2)):
        if idx % 2 == 0:
            shuffled.append(second_half[second_part_idx])
            second_part_idx += 1
        else:
            shuffled.append(first_half[first_part_idx])
            first_part_idx += 1
    cards = shuffled


pr_list = [fitst_card] + shuffled + [last_card]

print(pr_list)
