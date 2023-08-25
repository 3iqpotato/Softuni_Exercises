import tkinter

class ValueCannotBeNegative(Exception):
    pass

while True:
    n = int(input())
    if n < 0:
        raise ValueCannotBeNegative