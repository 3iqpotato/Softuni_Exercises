from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.astronaut_names = []
        self.planet_names = []
        self.completed_missions = 0
        self.not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if name in self.astronaut_names:
            return f"{name} is already added."

        astronaut = self.create_astronaut(astronaut_type, name)

        if astronaut:
            self.astronaut_repository.add(astronaut)
            self.astronaut_names.append(astronaut.name)
            return f"Successfully added {astronaut_type}: {name}."

        raise Exception("Astronaut type is not valid!")

    def add_planet(self, name: str, items: str):
        if name in self.planet_names:
            return f"{name} is already added."

        planet = Planet(name)
        planet_items = items.split(', ')

        planet.items = planet_items
        self.planet_repository.add(planet)
        self.planet_names.append(name)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)

        if astronaut:
            self.astronaut_names.remove(astronaut.name)
            self.astronaut_repository.remove(astronaut)

            return f"Astronaut {name} was retired!"

        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def capable_astronauts(self):
        astronauts_ready = []
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen > 30:
                astronauts_ready.append(astronaut)

        return astronauts_ready

    def send_on_mission(self, planet_name: str):

        planet = self.planet_repository.find_by_name(planet_name)

        if not planet:
            raise Exception("Invalid planet name!")

        astronauts_for_mission = self.capable_astronauts()

        if not astronauts_for_mission:
            raise Exception("You need at least one astronaut to explore the planet!")

        sorted_astronauts = sorted(astronauts_for_mission, key=lambda a: -a.oxygen)[:5]

        a_in_space = 0
        for astronaut in sorted_astronauts:
            if len(planet.items) == 0:
                break
            a_in_space += 1
            while astronaut.oxygen > 0 and len(planet.items) > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()

        if len(planet.items) == 0:
            self.completed_missions += 1
            return f"Planet: {planet_name} was explored. {a_in_space} astronauts participated in collecting items."

        self.not_completed_missions += 1
        return "Mission is not completed."

    def report(self):
        res = [f"{self.completed_missions} successful missions!\n"
                f"{self.not_completed_missions} missions were not completed!\n"
                f"Astronauts' info:"]

        for a in self.astronaut_repository.astronauts:
            backpack_items = ', '.join(a.backpack) if a.backpack else 'none'
            res.append(f"Name: {a.name}\n"
                        f"Oxygen: {a.oxygen}\n"
                        f"Backpack items: {backpack_items}")

        return "\n".join(res)

    @staticmethod
    def create_astronaut(astronaut_type, name):
        if astronaut_type == 'Biologist':
            return Biologist(name)
        elif astronaut_type == 'Geodesist':
            return Geodesist(name)
        elif astronaut_type == 'Meteorologist':
            return Meteorologist(name)


# s = SpaceStation()
# print(s.add_planet('baba', 'mql, bal, l, ok, l, l, l, l, l, dj, k, i, f, m, l, l, l, l, l, l, l, l, l, l, l, l, l, l, l, l'))
# print(s.add_astronaut('Meteorologist', 'koko'))
# print(s.add_astronaut('Meteorologist', 'bobi'))
# print(s.add_astronaut('Meteorologist', 'kikio'))
# print(s.add_astronaut('Meteorologist', 'kko'))
# print(s.add_astronaut('Meteorologist', 'kksdao'))
# print(s.add_astronaut('Meteorologist', 'kkydo'))
# print(s.add_planet('baba', 'a'))
# print(s.send_on_mission('baba'))
# print(s.report())
a = [1, 3]
print(a[:4])