list_nums = input().split()

while True:
    command = input().split()
    if command[0] == 'end':
        break
    if command[0] == 'exchange':
        num = int(command[1])
        first_half = []
        if num >= len(list_nums) or num < 0:
            print("Invalid index")
            continue
        for idx in range(num + 1):
            first_half.append(list_nums[0])
            list_nums.remove(list_nums[0])
        list_nums.extend(first_half)
        #print(list_nums)
    elif command[0] == 'max':
        if command[1] == 'even':
            has_even = False
            even_nums = []
            for number in list_nums:
                if int(number) % 2 == 0:
                    even_nums.append(int(number))
                    has_even = True
            if has_even:
                max_even = max(even_nums)
                x = ''
                for numb in range(len(list_nums)):
                    if int(list_nums[numb]) == int(max_even):
                        x = numb
                print(x)
            else:
                print("No matches")
        if command[1] == 'odd':
            has_odd = False
            odd_nums = []
            for number in list_nums:
                if int(number) % 2 != 0:
                    odd_nums.append(int(number))
                    has_odd = True
            if has_odd:
                max_odd = max(odd_nums)
                x = ''
                for numb in range(len(list_nums)):
                    if int(list_nums[numb]) == int(max_odd):
                        x = numb
                print(x)
            else:
                print("No matches")
    elif command[0] == 'min':
        if command[1] == 'even':
            has_even = False
            even_nums = []
            for number in list_nums:
                if int(number) % 2 == 0:
                    even_nums.append(int(number))
                    has_even = True
            if has_even:
                min_even = min(even_nums)
                x = ''
                for numb in range(len(list_nums)):
                    if int(list_nums[numb]) == int(min_even):
                        x = numb
                print(x)
            else:
                print("No matches")
        if command[1] == 'odd':
            has_odd = False
            odd_nums = []
            for number in list_nums:
                if int(number) % 2 != 0:
                    odd_nums.append(int(number))
                    has_odd = True
            if has_odd:
                min_odd = min(odd_nums)
                x = ''
                for numb in range(len(list_nums)):
                    if int(list_nums[numb]) == int(min_odd):
                        x = numb
                print(x)
            else:
                print("No matches")
    elif command[0] == 'first':
        if int(command[1]) <= 0:
            print("Invalid index")
            continue
        printed = False
        count = command[1]
        function = command[2]
        if function == 'even':
            first_numbers = []
            if int(count) > len(list_nums):
                print("Invalid count")
                continue
            for number in list_nums:
                if len(first_numbers) == int(count):
                    print(f'[{", ".join(first_numbers)}]')
                    printed = True
                    break
                if int(number) % 2 == 0:
                    first_numbers.append(number)
            if not printed:
                print(f'[{", ".join(first_numbers)}]')
        if function == 'odd':
            first_numbers = []
            if int(count) > len(list_nums):
                print("Invalid count")
                continue
            for number in list_nums:
                if len(first_numbers) == int(count):
                    print(f'[{", ".join(first_numbers)}]')
                    printed = True
                    break
                if int(number) % 2 != 0:
                    first_numbers.append(number)
            if not printed:
                print(f'[{", ".join(first_numbers)}]')
    elif command[0] == 'last':
        count = int(command[1])
        function = command[2]
        if count < 0:
            print('Invalid index')
            continue
        if count > len(list_nums):
            print("Invalid count")
            continue
        if count == 0:
            print('[]')
            continue
        if function == 'even':
            new_list = []
            for number in list_nums:
                if int(number) % 2 == 0:
                    new_list.append(str(number))
            if len(new_list) >= int(count):
                pr_list = new_list[-int(command[1]):]
                print(f'[{", ".join(pr_list)}]')
                continue
            else:
                print(f'[{", ".join(new_list)}]')
        if function == 'odd':
            new_list = []
            for number in list_nums:
                if int(number) % 2 != 0:
                    new_list.append(str(number))
            if len(new_list) >= int(count):
                pr_list = new_list[-int(command[1]):]
                print(f'[{", ".join(pr_list)}]')
                continue
            else:
                print(f'[{", ".join(new_list)}]')

print(f'[{", ".join(list_nums)}]')
