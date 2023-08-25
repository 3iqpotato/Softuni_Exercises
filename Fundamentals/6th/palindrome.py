def check(numbs):
    if str(numbs)[::-1] == str(n):
        return True
    else:
        return False




numbers = [int(x) for x in input().split(", ")]
for n in numbers:
    print(check(n))
