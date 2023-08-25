def exist(my_item, shop_list):
    if my_item in shop_list:
        return True
    return False


def is_valid(idx, sections):
    if 0 <= idx < len(sections):
        return True
    return False


initial_loot = input().split('|')
command = input().split()
while "Yohoho!" not in command:
    move = command.pop(0)
    if move == 'Loot':
        for item in command:
            if not exist(item, initial_loot):
                initial_loot.insert(0, item)
    elif move == "Drop":
        index = int(command[0])
        if is_valid(index, initial_loot):
            initial_loot.append(initial_loot.pop(index))
    elif move == "Steal":
        count = int(command[0])
        removed = []
        if is_valid(count, initial_loot):
            for _ in range(count):
                removed.insert(0, initial_loot.pop(-1))
            print(', '.join(removed))
        else:
            print(', '.join(initial_loot))
            initial_loot.clear()

    command = input().split()
if len(initial_loot) > 0:
    sum_of_len = sum(len(x) for x in initial_loot)
    average_gain = sum_of_len / len(initial_loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")