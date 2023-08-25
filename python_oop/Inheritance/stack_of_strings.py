class BaseStack:
    def __init__(self):
        self.data = []

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


class AddingElement(BaseStack):
    def push(self, element):
        self.data.append(element)


class PopingElement(BaseStack):
    def pop(self):
        return self.data.pop()


class Top(BaseStack):
    def top(self):
        return self.data[-1]


class IsEmpty(BaseStack):
    def is_empty(self):
        return True if not self.data else False


class Stack(AddingElement, PopingElement, Top, IsEmpty):
    pass


