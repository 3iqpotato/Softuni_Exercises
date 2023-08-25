class reverse_iter:
    def __init__(self, items):
        self.items = items
        self.curr_idx = 0


    def __iter__(self):
        return self

    def __next__(self):
        self.curr_idx -= 1
        if self.curr_idx < -len(self.items):
            raise StopIteration

        return self.items[self.curr_idx]




reversed_list = reverse_iter([1, 2, 3, 4, 5])
for item in reversed_list:
    print(item)
