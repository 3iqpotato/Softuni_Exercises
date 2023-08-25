def recursive_power(a, b):
    if b == 1:
        return a
    return a * recursive_power(a, b - 1)

print(recursive_power(2, 10))