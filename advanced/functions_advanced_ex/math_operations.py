from collections import deque

def math_operations(*args, **kwargs):
    c = 0
    for idx in args:
        key = list(kwargs.keys())[c % 4]
        if key == 'a':
            kwargs[key] += idx
        elif key == 's':
            kwargs[key] -= idx
        elif key == 'd':
            if idx != 0:
                kwargs[key] /= idx
        elif key == 'm':
            kwargs[key] *= idx

        c += 1

    return '\n'.join(f"{key}: {value:.1f}" for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])))

import unittest
class Tests(unittest.TestCase):
    def test(self):
        result = math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15)
        self.assertEqual(result.strip(), "d: 33.0\ns: 15.1\na: 9.1\nm: -58.5")

if __name__ == "__main__":
    unittest.main()
print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7,
d=33, m=15))
print(math_operations(6.0, a=0, s=0, d=5, m=0))

# dic = {'a': 1, 'B': 4}
# print(dic[0])