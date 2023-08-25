from project.tennis_player import TennisPlayer
from unittest import TestCase

class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.tennis_player = TennisPlayer('spas', 19, 3)

    def test_initialization_method(self):
        self.assertEqual('spas', self.tennis_player.name)
        self.assertEqual(19, self.tennis_player.age)
        self.assertEqual(3, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_name_prop(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = 'ko'

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = ''

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

        self.tennis_player.name = 'kok'
        self.assertEqual('kok', self.tennis_player.name)

    def test_age_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

        self.tennis_player.age = 18
        self.assertEqual(18, self.tennis_player.age)

    def test_add_new_win_method(self):
        self.tennis_player.add_new_win('kur')
        self.assertEqual(['kur'], self.tennis_player.wins)
        res = self.tennis_player.add_new_win('kur')
        self.assertEqual(res, f"kur has been already added to the list of wins!")
        self.tennis_player.add_new_win('kur1')
        self.assertEqual(['kur', 'kur1'], self.tennis_player.wins)

    def test_str_method(self):
        expected = f"Tennis Player: spas\n" \
               f"Age: 19\n" \
               f"Points: 3.0\n" \
               f"Tournaments won: "
        self.assertEqual(expected, str(self.tennis_player))
        self.tennis_player.add_new_win('kur')
        self.tennis_player.add_new_win('kur1')
        expected = f"Tennis Player: spas\n" \
               f"Age: 19\n" \
               f"Points: 3.0\n" \
               f"Tournaments won: kur, kur1"
        self.assertEqual(expected, str(self.tennis_player))

    def test_the_it_method(self):
        new_player = TennisPlayer('bobi', 19, 30)
        res = self.tennis_player.__lt__(new_player)
        self.assertEqual(f'bobi is a top seeded player and he/she is better than spas', res)
        self.tennis_player.points = 33
        res = self.tennis_player.__lt__(new_player)
        self.assertEqual(f'spas is a better player than bobi', res)