class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.cur_idx = -1


    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration

        self.number -= 1
        self.cur_idx += 1
        if self.cur_idx >= len(self.sequence):
            self.cur_idx = 0

        return self.sequence[self.cur_idx]

# test zero
import unittest

class Tests(unittest.TestCase):
    def test_zero(self):
        result = list(sequence_repeat('abc', 5))
        self.assertEqual(result, ['a', 'b', 'c', 'a', 'b'])

if __name__ == '__main__':
    unittest.main()


result = sequence_repeat('abc', 5)
for item in result:
 print(item, end ='')
