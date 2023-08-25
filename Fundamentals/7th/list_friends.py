def is_valid(idx, sections):
    if 0 <= idx < len(sections):
        return True
    return False


count_black = 0
lost_num = 0
friend_list = input().split(", ")
command = input().split()

while 'Report' not in command:
    move = command[0]
    if move == "Blacklist":
        name = command[1]
        if name in friend_list:
            x = friend_list.index(name)
            friend_list.pop(x)
            friend_list.insert(x, 'Blacklisted')
            print(f'{name} was blacklisted.')
            count_black += 1
        else:
            print(f"{name} was not found.")
    if move == 'Error':
        index = int(command[1])
        if is_valid(index, friend_list):
            if friend_list[index] != 'Lost' and friend_list[index] != 'Blacklisted':
                print(f'{friend_list[index]} was lost due to an error.')
                friend_list[index] = 'Lost'
                lost_num += 1
    if move == 'Change':
        index = int(command[1])
        new_name = command[2]
        if is_valid(index, friend_list):
            print(f"{friend_list[index]} changed his username to {new_name}.")
            friend_list[index] = new_name
    command = input().split()

print(f"Blacklisted names: {count_black}")
print(f"Lost names: {lost_num}")
print(' '.join(friend_list))