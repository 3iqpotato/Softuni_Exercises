from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_initialization(self):
        expected = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual(expected, self.toy_store.toy_shelf)

    def test_add_method(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('h', 'kur')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

        expected = {
            "A": None,
            "B": None,
            "C": 'kur',
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        res = self.toy_store.add_toy('C', 'kur')
        self.assertEqual(expected, self.toy_store.toy_shelf)
        self.assertEqual(f"Toy:kur placed successfully!", res)

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('C', 'kur')

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('C', 'kor')

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_remove_method(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('K', 'kok')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

        self.toy_store.add_toy('C', 'kur')

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('C', 'kor')

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

        res = self.toy_store.remove_toy('C', 'kur')
        self.assertEqual(f"Remove toy:kur successfully!", res)
        expected = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(expected, self.toy_store.toy_shelf)