num_lines = int(input())
rolls = []
for roll in range(num_lines):
    rolls.append(list(int(x) for x in input().split()))
broken_ships = 0
battle_roll = input().split()
for battles in battle_roll:
    battle = battles.split('-')
    row = int(battle[0])
    col = int(battle[1])
    row_ship = list(rolls[row])
    # ship = int(row_ship[col])
    if int(row_ship[col]) > 0:
        rolls[row][col] = int(rolls[row][col]) - 1
        # row_ship[col] = int(row_ship[col]) - 1
        if int(rolls[row][col]) == 0:
            broken_ships += 1

print(broken_ships)


# 3
# 1 0 0 1
# 2 0 0 0
# 0 3 0 1
# 0-0 1-0 2-1 2-1 2-1 1-1 2-1
# 5
# 1 0 5 0 1
# 6 3 9 0 0
# 7 9 4 3 2
# 1 0 0 4 9
# 5 6 0 3 5
# 0-1 0-2 0-2 0-2 0-2 0-2 3-0