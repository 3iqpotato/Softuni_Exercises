from project.mammal import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('KO', 'zemno', 'burrr')

    def test_initialization(self):
        self.assertEqual('KO', self.mammal.name)
        self.assertEqual('zemno', self.mammal.type)
        self.assertEqual('burrr', self.mammal.sound)
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_making_sound(self):
        self.assertEqual(f"KO makes burrr", self.mammal.make_sound())

    def test_info_method(self):
        self.assertEqual("KO is of type zemno", self.mammal.info())

if __name__ == '__main__':
    main()