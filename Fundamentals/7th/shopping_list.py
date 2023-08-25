def exist(my_item, shop_list):
    if my_item in shop_list:
        return True
    return False


sopping_list = input().split("!")

while True:
    command = input()
    if "Go Shopping!" in command:
        break
    command = command.split()
    move = command[0]
    item = command[1]
    if move == "Urgent":
        if not exist(item, sopping_list):
            sopping_list.insert(0, item)

    elif move == "Unnecessary":
        if exist(item, sopping_list):
            sopping_list.remove(item)

    elif move == "Correct":
        new_item = command[2]
        if exist(item, sopping_list):
            for i in range(len(sopping_list)):
                if sopping_list[i] == item:
                    sopping_list.remove(item)
                    sopping_list.insert(i, new_item)

    elif move == "Rearrange":
        if exist(item, sopping_list):
            sopping_list.remove(item)
            sopping_list.append(item)
print(', '.join(sopping_list))