phones_list = input().split(', ')
command = input().split(' - ')

while 'End' not in command:
    move = command[0]
    phone = command[1]
    if move == 'Add':
        if phone not in phones_list:
            phones_list.append(phone)
    if move == 'Remove':
        if phone in phones_list:
            phones_list.remove(phone)
    if move == "Bonus phone":
        phone = phone.split(':')
        if phone[0] in phones_list:
            phones_list.insert(phones_list.index(phone[0]) + 1, phone[1])
    if move == 'Last':
        if phone in phones_list:
            phones_list.append(phones_list.pop(phones_list.index(phone)))
    command = input().split(' - ')

print(', '.join(phones_list))