class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class Testlist(unittest.TestCase):
    def setUp(self) -> None:
        self.my_List = IntegerList()

    def test_init_method_with_diferent_nums(self):
        new_list = IntegerList(3, 4, 5, 6)
        self.assertEqual([3, 4, 5, 6], new_list.get_data())

        new_list = IntegerList(3, 4, 5, 6.5)
        self.assertEqual([3, 4, 5], new_list.get_data())

        new_list = IntegerList(3, 4, 5, 'da')
        self.assertEqual([3, 4, 5], new_list.get_data())

    def test_add_method(self):
        self.assertEqual([], self.my_List.get_data())
        self.my_List.add(3)
        self.assertEqual([3], self.my_List.get_data())

        with self.assertRaises(ValueError) as ex:
            self.my_List.add('da')

        self.assertEqual("Element is not Integer", ex.exception.args[0])

        with self.assertRaises(ValueError) as ex:
            self.my_List.add(4.4)

        self.assertEqual("Element is not Integer", ex.exception.args[0])

        with self.assertRaises(ValueError) as ex:
            self.my_List.add((4, 6, 7))

        self.assertEqual("Element is not Integer", ex.exception.args[0])

    def test_remove_index_method(self):
        self.assertEqual([], self.my_List.get_data())
        self.my_List.add(3)
        self.assertEqual([3], self.my_List.get_data())

        self.my_List.remove_index(0)
        self.assertEqual([], self.my_List.get_data())

        with self.assertRaises(IndexError) as ex:
            self.my_List.remove_index(0)

        self.assertEqual("Index is out of range", ex.exception.args[0])

    def test_remove_idx_with_more_nums(self):
        self.my_List.add(3)
        self.my_List.add(3)
        self.my_List.add(3)
        self.my_List.add(3)

        self.my_List.remove_index(3)
        self.assertEqual([3, 3, 3], self.my_List.get_data())

        with self.assertRaises(IndexError) as ex:
            self.my_List.remove_index(7)

        self.assertEqual("Index is out of range", ex.exception.args[0])

    def test_get_method(self):
        self.my_List.add(3)
        res = self.my_List.get(0)
        self.assertEqual(3, res)

        with self.assertRaises(IndexError) as ex:
            self.my_List.get(1)

        self.assertEqual("Index is out of range", ex.exception.args[0])

        with self.assertRaises(IndexError) as ex:
            self.my_List.get(3)

        self.assertEqual("Index is out of range", ex.exception.args[0])

    def test_insert_method(self):
        self.my_List.add(3)
        self.my_List.add(3)
        self.my_List.add(3)

        self.my_List.insert(1, 6)
        self.assertEqual([3, 6, 3, 3], self.my_List.get_data())

        with self.assertRaises(IndexError) as ex:
            self.my_List.insert(4, 7)

        self.assertEqual("Index is out of range", ex.exception.args[0])

        with self.assertRaises(IndexError) as ex:
            self.my_List.insert(15, 7)

        self.assertEqual("Index is out of range", ex.exception.args[0])

        with self.assertRaises(ValueError) as ex:
            self.my_List.insert(1, 'kur')

        self.assertEqual("Element is not Integer", ex.exception.args[0])

        with self.assertRaises(ValueError) as ex:
            self.my_List.insert(1, 2.3)

        self.assertEqual("Element is not Integer", ex.exception.args[0])

    def test_get_biggest_method(self):
        self.my_List.add(3)
        self.my_List.add(6)
        self.my_List.add(9)

        self.assertEqual(9, self.my_List.get_biggest())

    def test_get_index_method(self):
        self.my_List.add(3)
        self.my_List.add(6)
        self.my_List.add(9)

        res = self.my_List.get_index(9)
        self.assertEqual(2, res)

if __name__ == '__main__':
    unittest.main()