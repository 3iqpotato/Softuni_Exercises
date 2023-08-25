num = int(input())

for thou in range(1, 10):
    for hun in range(1, 10):
        for ten in range(1, 10):
            for unit in range(1, 10):
                if num % thou == 0 and num % hun == 0 and num % ten == 0 and num % unit == 0:
                    number = f'{thou}{hun}{ten}{unit}'
                    print(number, end=' ')


