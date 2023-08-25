class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)

from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self) -> None:
        self.car = Car('kola', 'lada', 3, 33)

    def test_car_initialization(self):
        self.assertEqual('kola', self.car.make)
        self.assertEqual('lada', self.car.model)
        self.assertEqual(3, self.car.fuel_consumption)
        self.assertEqual(33, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_make_property(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fueL_consumption_property_with_equal_num(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fueL_consumption_property_with_less_num(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -3

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_property(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -3

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fueL_capacity_property_with_equal_num(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_property(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -3

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refueling_the_car_with_negative_num(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-3)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refueling_with_more_fuel(self):
        self.car.refuel(300)
        self.assertEqual(33, self.car.fuel_amount)

    def test_refuel_car_with_less_fuel(self):
        self.car.refuel(13)
        self.assertEqual(13, self.car.fuel_amount)

    def test_driving_with_less_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_driving_ith_enough_fuel(self):
        self.car.fuel_amount = 30
        self.car.drive(3)
        self.assertEqual(30-0.09, self.car.fuel_amount)

if __name__ == '__main__':
   main()