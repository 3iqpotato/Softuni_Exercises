from project.truck_driver import TruckDriver
from unittest import TestCase


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.truck_driver = TruckDriver('pepi', 10)

    def test_check_initialization(self):
        self.assertEqual('pepi', self.truck_driver.name)
        self.assertEqual(10, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_earned_money_prop(self):
        with self.assertRaises(ValueError) as ve:
            self.truck_driver.earned_money = -1

        self.assertEqual(f"pepi went bankrupt.", str(ve.exception))

    def test_adding_cargo_offer(self):
        res = self.truck_driver.add_cargo_offer('pleven', 30)
        self.assertEqual({'pleven': 30}, self.truck_driver.available_cargos)
        self.assertEqual(res, f"Cargo for 30 to pleven was added as an offer.")

        with self.assertRaises(Exception) as ve:
            self.truck_driver.add_cargo_offer('pleven', 30)

        self.assertEqual("Cargo offer is already added.", str(ve.exception))

        self.truck_driver.add_cargo_offer('plevena', 30)
        self.assertEqual({'pleven': 30, 'plevena': 30}, self.truck_driver.available_cargos)

    def test_drive_best_cargo_offer(self):
        res = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(res, "There are no offers available.")
        self.truck_driver.add_cargo_offer('plevena', 30)
        self.truck_driver.add_cargo_offer('pleven', 30)
        res = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(res, f"pepi is driving 30 to plevena.")
        self.assertEqual(30, self.truck_driver.miles)
        self.assertEqual(300, self.truck_driver.earned_money)
        self.truck_driver.add_cargo_offer('plovdiv', 11000)
        res = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(res, f"pepi is driving 11000 to plovdiv.")
        self.assertEqual(11030, self.truck_driver.miles)
        self.assertEqual(97925, self.truck_driver.earned_money)

    def test_repr_method(self):
        self.assertEqual('pepi has 0 miles behind his back.', self.truck_driver.__repr__())
        self.truck_driver.add_cargo_offer('plevena', 30)
        self.truck_driver.drive_best_cargo_offer()
        self.assertEqual('pepi has 30 miles behind his back.', self.truck_driver.__repr__())


