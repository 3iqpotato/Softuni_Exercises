def type_check(type_my):
    def decorator(function):
        def wrapper(*args):
            for l in args:
                if not isinstance(l, type_my):
                    return 'Bad Type'
            return function(*args)

        return wrapper
    return decorator

@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))
