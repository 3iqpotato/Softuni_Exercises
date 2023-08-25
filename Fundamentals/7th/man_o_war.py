def is_valid(idx, sections):
    if 0 <= idx < len(sections):
        return True
    return False


pirate_ship_stats = [int(x) for x in input().split('>')]
warship_stats = [int(x) for x in input().split('>')]
max_health_capacity = int(input())

sinked = False
while not sinked:
    command = input().split()
    if "Retire" in command:
        break
    move = command[0]
    if move == 'Fire':
        index = int(command[1])
        damage = int(command[2])
        if not is_valid(index, warship_stats):
            continue

        warship_stats[index] -= damage
        if warship_stats[index] <= 0:
            sinked = True
            print("You won! The enemy ship has sunken.")
            break

    elif move == 'Defend':
        start_idx = int(command[1])
        end_idx = int(command[2])
        damage = int(command[3])
        if not is_valid(start_idx, pirate_ship_stats) or not is_valid(end_idx, pirate_ship_stats):
            continue
        else:
            for section in range(start_idx, end_idx + 1):
                pirate_ship_stats[section] -= damage
                if pirate_ship_stats[section] <= 0:
                    sinked = True
                    print("You lost! The pirate ship has sunken.")
                    break
    elif move == 'Repair':
        index = int(command[1])
        health = int(command[2])
        if not is_valid(index, pirate_ship_stats):
            continue
        else:
            pirate_ship_stats[index] = min(max_health_capacity, pirate_ship_stats[index] + health)
    elif move == 'Status':
        bad_health = max_health_capacity * 0.2
        count = 0
        for section in pirate_ship_stats:
            if section < bad_health:
                count += 1
        print(f"{count} sections need repair.")

if not sinked:
    print(f"Pirate ship status: {sum(pirate_ship_stats)}")
    print(f"Warship status: {sum(warship_stats)}")
