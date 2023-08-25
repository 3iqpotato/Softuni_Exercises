class Example:
    text = 'Hello'
    def print_text(self):
        return 'SoftUni'

Example.text # attribute reference
Example.print_text # attribute reference
x = Example()

class MyClass:
    def say_hello(self):
        return 'Hello'
x = MyClass()
print(x.say_hello()) # conventional way
print(MyClass.say_hello(x))