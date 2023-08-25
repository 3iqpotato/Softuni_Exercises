moves = {
    '-': lambda x, y: x - y,
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x ** y,
}


def mat(a, b, sign):
    return moves[sign](a, b)



