def read_next(*args):
    for something in args:
        yield from something




for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

l = [1, 2, 3]
for _ in range(2):
    print()