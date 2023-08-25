from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot('3', 'Military', 3, 300)

    def test_robots_initialization(self):
        self.assertEqual('3', self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(3, self.robot.available_capacity)
        self.assertEqual(300, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)
        self.assertEqual(1.5, self.robot.PRICE_INCREMENT)
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], self.robot.ALLOWED_CATEGORIES)

    def test_category_property(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'lolo'

        self.assertEqual(f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'", str(ve.exception))

        self.robot.category = 'Humanoids'
        self.assertEqual('Humanoids', self.robot.category)

    def test_price_property(self):

        self.robot.price = 0
        self.assertEqual(0, self.robot.price)

        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrading_the_robot_with_not_valid_part(self):
        res = self.robot.upgrade('kur', 100)
        self.assertEqual('kur', self.robot.hardware_upgrades[0])
        self.assertEqual(100*1.5+300, self.robot.price)
        self.assertEqual(f'Robot 3 was upgraded with kur.', res)

        res = self.robot.upgrade('kor', 100)
        self.assertEqual('kor', self.robot.hardware_upgrades[-1])
        self.assertEqual(100 * 1.5 + 100*1.5+300, self.robot.price)
        self.assertEqual(f'Robot 3 was upgraded with kor.', res)

    def test_upgrade_robot_with_part_he_has(self):
        self.robot.hardware_upgrades.append('kur')
        res = self.robot.upgrade('kur', 100)
        self.assertEqual(300, self.robot.price)

        self.assertEqual(f"Robot 3 was not upgraded.", res)

    def test_updating_robot_without_software_updates(self):
        res = self.robot.update(10, 1)
        self.assertEqual(10, self.robot.software_updates[0])
        self.assertEqual(2, self.robot.available_capacity)
        self.assertEqual(f'Robot 3 was updated to version 10.', res)

        res = self.robot.update(11, 1)
        self.assertEqual(11, self.robot.software_updates[-1])
        self.assertEqual(1, self.robot.available_capacity)
        self.assertEqual(f'Robot 3 was updated to version 11.', res)

        res = self.robot.update(10, 1)
        self.assertEqual(11, self.robot.software_updates[-1])
        self.assertEqual(1, self.robot.available_capacity)
        self.assertEqual(f"Robot 3 was not updated.", res)

    def test_gt_method(self):
        new_robot = Robot('2', 'Humanoids', 10, 100)
        res = self.robot.__gt__(new_robot)
        self.assertEqual(f'Robot with ID 3 is more expensive than Robot with ID 2.', res)

        new_robot.price = 300
        res = self.robot.__gt__(new_robot)
        self.assertEqual(f'Robot with ID 3 costs equal to Robot with ID 2.', res)

        new_robot.price = 400
        res = self.robot.__gt__(new_robot)
        self.assertEqual(f'Robot with ID 3 is cheaper than Robot with ID 2.', res)