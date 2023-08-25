from typing import List

from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []
        self.car_models = []
        self.driver_names = []
        self.race_names = []

    @staticmethod
    def creating_car(car_t, model, speed_l):
        if car_t == 'SportsCar':
            return SportsCar(model, speed_l)

        if car_t == 'MuscleCar':
            return MuscleCar(model, speed_l)

    def find_car(self, car_type):
        cars = []
        if car_type in ["MuscleCar", "SportsCar"]:
            for car in self.cars:
                if car.__class__.__name__ == car_type and not car.is_taken:
                    cars.append(car)

        if cars:
            return cars[-1]

        raise Exception(f"Car {car_type} could not be found!")

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if model in self.car_models:
            raise Exception(f"Car {model} is already created!")

        car = self.creating_car(car_type, model, speed_limit)
        if car:
            self.car_models.append(model)
            self.cars.append(car)
            return f'{car_type} {model} is created.'

    def create_driver(self, driver_name: str):
        if driver_name in self.driver_names:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)

        if driver:
            self.driver_names.append(driver_name)
            self.drivers.append(driver)
            return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if race_name in self.race_names:
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)

        if race:
            self.race_names.append(race_name)
            self.races.append(race)
            return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if driver_name not in self.driver_names:
            raise Exception(f"Driver {driver_name} could not be found!")

        driver = [d for d in self.drivers if d.name == driver_name][0]
        car = self.find_car(car_type)

        if driver.car:
            old_car_model = driver.car.model
            driver.car.is_taken = False
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_car_model} to {car.model}."

        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if race_name not in self.race_names:
            raise Exception(f"Race {race_name} could not be found!") #TODO moze da iskat samo v listovete s race da se proveri

        if driver_name not in self.driver_names:
            raise Exception(f"Driver {driver_name} could not be found!")#TODO moze da iskat samo v listovete s driveri da se proveri

        # try:
        race = [r for r in self.races if r.name == race_name][0]
        # except IndexError:
        #     raise Exception(f"Race {race_name} could not be found!")

        # try:
        driver = [d for d in self.drivers if d.name == driver_name][0]
        # except IndexError:
        #     raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        if race_name not in self.race_names:
            raise Exception(f"Race {race_name} could not be found!")

        race = [r for r in self.races if r.name == race_name][0]

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = self.race_winners(race)

        res = []
        for driver in winners:
            driver.number_of_wins += 1
            res.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return '\n'.join(res)

    @staticmethod
    def race_winners(race) -> List[Driver]:
        winners = sorted(race.drivers, key=lambda d: -d.car.speed_limit)[:3]
        return winners

# a = Controller()
# print(a.create_driver('koko'))
# print(a.create_driver('kotka'))
# print(a.create_driver('kokos'))
# print(a.create_car('SportsCar', 'lada', 500))
# print(a.create_car('SportsCar', 'lada 007', 550))
# print(a.create_car('SportsCar', 'lada 2007', 570))
# print(a.create_car('SportsCar', 'lada 2107', 600))
# print(a.add_car_to_driver('kotka', 'SportsCar'))
#
# print(a.add_car_to_driver('koko', 'SportsCar'))
# print(a.create_driver('bobi'))
# print(a.add_car_to_driver('bobi', 'SportsCar'))
# print(a.add_car_to_driver('koko', 'SportsCar'))
# print(a.add_car_to_driver('kokos', 'SportsCar'))
# print(a.create_race('poligon'))
# print(a.add_driver_to_race('poligon', 'kokos'))
# print(a.add_driver_to_race('poligon', 'koko'))
# print(a.add_driver_to_race('poligon', 'bobi'))
# print(a.add_driver_to_race('poligon', 'kotka'))

#
# print(a.start_race('poligon'))