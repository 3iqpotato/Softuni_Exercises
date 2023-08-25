def exist(my_item, shop_list):
    if my_item in shop_list:
        return True
    return False


start_items = input().split(', ')

while True:
    command = input().split(' - ')
    if command[0] == "Craft!":
        break
    move = command[0]
    item = command[1]
    if move == 'Collect':
        if not exist(item, start_items):
            start_items.append(item)

    elif move == 'Drop':
        if exist(item, start_items):
            start_items.remove(item)

    elif move == 'Combine Items':
        items = item.split(':')
        old_item = items[0]
        new_item = items[1]
        if exist(old_item, start_items):
            idx = start_items.index(old_item)
            start_items.insert(idx + 1, new_item)
    elif move == 'Renew':
        if exist(item, start_items):
            idx = start_items.index(item)
            start_items.append(start_items.pop(idx))
print(', '.join(start_items))

