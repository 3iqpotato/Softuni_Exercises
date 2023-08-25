from project.second_hand_car import SecondHandCar
from unittest import TestCase


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar('lada', 'sport', 90000, 333)

    def test_initialization(self):
        self.assertEqual('lada', self.car.model)
        self.assertEqual('sport', self.car.car_type)
        self.assertEqual(90000, self.car.mileage)
        self.assertEqual(333, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_properties(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car.price = 0

        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

        self.car.price = 2
        self.assertEqual(2, self.car.price)

        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 99

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

        self.car.mileage = 101
        self.assertEqual(101, self.car.mileage)

    def test_set_promotion_price_method(self):
        res = self.car.set_promotional_price(332)
        self.assertEqual(332, self.car.price)
        self.assertEqual('The promotional price has been successfully set.', res)

        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(333)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(334)

        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_need_repair_method(self):
        self.car.price = 100
        res = self.car.need_repair(51, 'smazka')
        self.assertEqual('Repair is impossible!', res)
        self.assertEqual([], self.car.repairs)
        self.assertEqual(100, self.car.price)

        res = self.car.need_repair(30, 'novo butalo')
        self.assertEqual(f'Price has been increased due to repair charges.', res)
        self.assertEqual(130, self.car.price)
        self.assertEqual(['novo butalo'], self.car.repairs)

        res = self.car.need_repair(40, 'kotka')
        self.assertEqual(f'Price has been increased due to repair charges.', res)
        self.assertEqual(170, self.car.price)
        self.assertEqual(['novo butalo', 'kotka'], self.car.repairs)

    def test_the_gt_method(self):
        car1 = SecondHandCar('dacia', 'bavna', 100000, 300)
        res = self.car.__gt__(car1)
        self.assertEqual('Cars cannot be compared. Type mismatch!', res)
        car2 = SecondHandCar('dacia', 'sport', 100000, 333)
        res = self.car.__gt__(car2)
        self.assertEqual(False, res)
        car2.price=332
        res = self.car.__gt__(car2)
        self.assertEqual(True, res)

    def test_str_method(self):
        expected = f"""Model lada | Type sport | Milage 90000km
Current price: 333.00 | Number of Repairs: 0"""

        self.assertEqual(expected, str(self.car))
