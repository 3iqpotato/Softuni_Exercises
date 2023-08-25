from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    HORSE_TYPES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if self.check_if_horse_exist(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")

        try:
            horse = self.HORSE_TYPES[horse_type](horse_name, horse_speed)
        except KeyError:
            return None

        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.check_if_jockey_exist(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.check_if_race_exist(race_type):
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):#TODO last horse
        if not self.check_if_jockey_exist(jockey_name):
            raise Exception(f"Jockey {jockey_name} could not be found!")

        jockey = self.find_jockey(jockey_name)

        horse = self.find_available_horse(horse_type)
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        if not self.check_if_race_exist(race_type):
            raise Exception(f"Race {race_type} could not be found!")

        race = self.find_race_by_type(race_type)

        if not self.check_if_jockey_exist(jockey_name):
            raise Exception(f"Jockey {jockey_name} could not be found!")

        jockey = self.find_jockey(jockey_name)

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        if not self.check_if_race_exist(race_type):
            raise Exception(f"Race {race_type} could not be found!")

        race = self.find_race_by_type(race_type)

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = self.find_winner(race)

        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."

    def check_if_horse_exist(self, horse_name):
        for horse in self.horses:
            if horse.name == horse_name:
                return True
        return False

    def check_if_jockey_exist(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return True
        return False

    def check_if_race_exist(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return True
        return False

    def find_jockey(self, name):
        return [j for j in self.jockeys if j.name == name][0]

    def find_available_horse(self, horse_type):
        horses = [h for h in self.horses if h.__class__.__name__ == horse_type and not h.is_taken]
        if horses:
            return horses[-1]

        return None

    def find_race_by_type(self, type_race):
        return [r for r in self.horse_races if r.race_type == type_race][0]

    @staticmethod
    def find_winner(race: HorseRace) -> Jockey:
        sorted_racers = sorted(race.jockeys, key=lambda j: -j.horse.speed)
        return sorted_racers[0]


# a = HorseRaceApp()
# print(a.add_horse('Thoroughbred', 'koko', 120))
# print(a.add_horse('Thoroughbred', 'koki', 123))
# print(a.add_jockey('dada', 18))
# print(a.add_jockey('koko', 18))
# print(a.create_horse_race('Winter'))
# print(a.add_horse_to_jockey('dada', 'Thoroughbred'))
# print(a.add_horse_to_jockey('koko', 'Thoroughbred'))
# print(a.add_jockey_to_horse_race('Winter', 'dada'))
# print(a.add_jockey_to_horse_race('Winter', 'koko'))
# print(a.start_horse_race('Winter'))