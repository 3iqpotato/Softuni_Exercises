class vowels:
    def __init__(self, text):
        self.text = text
        self.vowels = ['a', 'i', 'o', 'e', 'u', 'y']
        self.curr_idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.curr_idx += 1

        if self.curr_idx == len(self.text):
            raise StopIteration

        letter = self.text[self.curr_idx]
        if letter.lower() in self.vowels:
            return letter

        return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
 print(char)