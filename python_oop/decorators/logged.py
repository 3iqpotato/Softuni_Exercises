def logged(function):
        def decorator(*args):

            return f"you called {function.__name__}({', '.join([str(l) for l in args])})\n"\
                    f"it returned {function(*args)}"

        return decorator



@logged
def sum_func(a, b):
 return a + b
print(sum_func(1, 4))
