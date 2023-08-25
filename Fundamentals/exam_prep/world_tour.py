def is_valid(idx, password):
    return 0 <= idx < len(password)


all_destinations = input()
while True:
    input_line = input().split(':')
    if "Travel" in input_line:
        break
    command = input_line[0]
    if command == 'Add Stop':
        idx = int(input_line[1])
        string = input_line[2]
        if is_valid(idx, all_destinations):
            all_destinations = all_destinations[:idx] + string + all_destinations[idx:]

    elif command == 'Remove Stop':
        start = int(input_line[1])
        end = int(input_line[2])
        if is_valid(start, all_destinations) and is_valid(end, all_destinations):
            all_destinations = all_destinations[:start] + all_destinations[end+1:]
    else:
        old_str = input_line[1]
        new_str = input_line[2]
        if old_str in all_destinations:
            all_destinations = all_destinations.replace(old_str, new_str)
    print(all_destinations)
print(f'Ready for world tour! Planned stops: {all_destinations}')

# Hawai::Cyprys-Greece
# Add Stop:7:Rome
# Remove Stop:11:16
# Switch:Hawai:Bulgaria
# Travel