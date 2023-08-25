command = ['last', '0', 'odd']
list_nums = [1, 2, 3, 4, 5, 6, 7]

if command[0] == 'last':
    if int(command[1]) <= 0:
        print("Invalid index")
    if int(command[1]) > len(list_nums):
        print("Invalid count")
        exit()

    count = command[1]
    function = command[2]
    new_list = []
    pr_list = []
    if function == 'even':
        for num in list_nums:
            if int(num) % 2 == 0:
                new_list.append(str(num))
        if len(new_list) < int(count):

            print(f'[{", ".join(new_list)}]')
        else:
            pr_list = new_list[-int(command[1]):]
            print(f'[{", ".join(pr_list)}]')

    if function == 'odd':
        for num in list_nums:
            if int(num) % 2 != 0:
                new_list.append(str(num))
        if len(new_list) < int(count):

            print(f'[{", ".join(new_list)}]')
        else:
            pr_list = new_list[-int(command[1]):]
            print(f'[{", ".join(pr_list)}]')