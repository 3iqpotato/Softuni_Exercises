class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.num = 0
        self.curr_nums = -1
        self.nums = [n*step for n in range(count)]

    def __iter__(self):
        return self

    def __next__(self):
        self.curr_nums += 1

        if self.curr_nums == self.count:
            raise StopIteration('a')

        return self.nums[self.curr_nums]


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(-10, 5)
for number in numbers:
    print(number)

class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration

        curr_number = self.start
        self.start += 1
        self.count -= 1

        return curr_number * self.step


numbers = take_skip(2, 6)
for number in numbers:
    print(number)


