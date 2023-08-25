elements = input().split()
command = input().split()
times = 0
win = False
while 'end' not in command:
    times += 1
    first = int(command[0])
    second = int(command[1])
    if first == second or first >= len(elements) or second >= len(elements) or first < 0 or second < 0:
        mid = int(len(elements) / 2)
        add = f'-{times}a'
        elements.insert(mid, add)
        elements.insert(mid, add)
        print('Invalid input! Adding additional elements to the board')
        command = input().split()
        continue

    if elements[first] == elements[second]:
        print(f"Congrats! You have found matching elements - {elements[first]}!")
        a = elements[first]
        b = elements[second]
        elements.remove(a)
        elements.remove(b)
    else:
        print("Try again!")
    if len(elements) <= 0:
        print(f"You have won in {times} turns!")
        win = True
        break
    command = input().split()
if not win:
    print("Sorry you lose :(")
    print(' '.join(elements))
