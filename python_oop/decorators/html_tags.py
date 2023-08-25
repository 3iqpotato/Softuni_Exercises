def tags(tag):
    def designer(func):
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"

        return wrapper

    return designer



# test first zero
import unittest

class TagsTests(unittest.TestCase):
    def test_zero_first(self):
        @tags('p')
        def join_strings(*args):
            return "".join(args)
        self.assertEqual(join_strings("Hello", " you!"), '<p>Hello you!</p>')

if __name__ == '__main__':
    unittest.main()
