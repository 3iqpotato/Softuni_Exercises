max1 = int(input())
max2 = int(input())
max3 = int(input())

for first in range(1, max1 + 1):
    for sec in range(2, max2 + 1):
        for third in range(1, max3 + 1):
            if first % 2 == 0 and third % 2 == 0:
                times = 0
                prime = 0
                for n in range(1, sec + 1):
                    core = sec % n
                    if core == 0:
                        times += 1
                if times == 2:
                    prime += sec
                else:
                    continue
                print(f'{first} {prime} {third}')