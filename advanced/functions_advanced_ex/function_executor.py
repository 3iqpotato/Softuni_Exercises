def func_executor(*args):
    res = []
    for name, things in args:
        res.append(f"{name.__name__} - {name(*things)}")

    return '\n'.join(res)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2



print(func_executor(
 (sum_numbers, (1, 2)),
 (multiply_numbers, (2, 4))
))
