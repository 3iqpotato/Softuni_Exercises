from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(30, 300)

    def test_initialization(self):
        self.assertEqual(30, self.vehicle.fuel)
        self.assertEqual(30, self.vehicle.capacity)
        self.assertEqual(300, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_driving_with_less_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_driving_with_enough_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(30-12.5, self.vehicle.fuel)

    def test_test_refueling_with_more_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(300)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refueling_with_less_fuel(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(5)
        self.assertEqual(22.5, self.vehicle.fuel)

    def test_str_method(self):
        expected = f"The vehicle has 300 " \
               f"horse power with 30 fuel left and 1.25 fuel consumption"
        actual = str(self.vehicle)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()