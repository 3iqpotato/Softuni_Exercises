from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('kok', 1, 30, 30)
        self.enemy = Hero('bob', 1, 20, 20)

    def test_initialization(self):
        self.assertEqual('kok', self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(30, self.hero.health)
        self.assertEqual(30, self.hero.damage)

    def test_battle_with_same_username(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_hero_hp_zero(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_with_enemy_hp_zero(self):
        self.enemy.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(f"You cannot fight bob. He needs to rest", str(ex.exception))

    def test_battle_when_they_both_die(self):
        self.enemy.health = 30
        self.enemy.damage = 30
        res = self.hero.battle(self.enemy)
        self.assertEqual('Draw', res)

    def test_battle_when_hero_wins(self):
        res = self.hero.battle(self.enemy)
        self.assertEqual('You win', res)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(15, self.hero.health)
        self.assertEqual(35, self.hero.damage)

    def test_battle_when_enemy_wins(self):
        self.enemy.health = 100
        self.enemy.damage = 100
        res = self.hero.battle(self.enemy)
        self.assertEqual('You lose', res)
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(75, self.enemy.health)
        self.assertEqual(105, self.enemy.damage)

    def test_str_method(self):
        expected = f"Hero kok: 1 lvl\n" \
               f"Health: 30\n" \
               f"Damage: 30\n"
        actual = str(self.hero)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    main()