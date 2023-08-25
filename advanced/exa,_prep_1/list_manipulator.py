from collections import deque


def list_manipulator(*args):
    args = deque(args)
    my_list, com, where, *digits = args
    my_list = deque(my_list)

    if com == 'add':
        if where == 'end':
            for el in digits:
                my_list.append(el)

        elif where == 'beginning':
            for el in digits:
                digits.extend(my_list)
                return digits
    if com == 'remove':
        if where == 'end':
            if digits:
                n = digits[0]

                for _ in range(n):
                    my_list.pop()
            else:
                my_list.pop()

        elif where == 'beginning':
            if digits:
                n = digits[0]

                for _ in range(n):
                    my_list.popleft()
            else:
                my_list.popleft()

    return list(my_list)


# print(list_manipulator([1,2,3], "remove", "end"))
# print(list_manipulator([1,2,3], "remove", "beginning"))
# print(list_manipulator([1,2,3], "add", "beginning", 20))
# print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

