from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.aquariums = []
        self.decorations_repository = DecorationRepository()

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == 'FreshwaterAquarium':
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
        elif aquarium_type == 'SaltwaterAquarium':
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
        else:
            return "Invalid aquarium type."

        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type == 'Ornament':
            self.decorations_repository.decorations.append(Ornament())
        elif decoration_type == 'Plant':
            self.decorations_repository.decorations.append(Plant())
        else:
            return "Invalid decoration type."

        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):

        my_aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."

        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."

        my_aquarium.add_decoration(decoration)
        self.decorations_repository.decorations.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]

        if fish_type == 'FreshwaterFish':
            fish = FreshwaterFish(fish_name, fish_species, price)

            if aquarium.__class__.__name__ == 'FreshwaterAquarium':
                return aquarium.add_fish(fish)
            return "Water not suitable."

        elif fish_type == 'SaltwaterFish':
            fish = SaltwaterFish(fish_name, fish_species, price)

            if aquarium.__class__.__name__ == 'SaltwaterAquarium':
                return aquarium.add_fish(fish)
            return "Water not suitable."

        else:
            return f"There isn't a fish of type {fish_type}."

    def feed_fish(self, aquarium_name: str):
        my_aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        my_aquarium.feed()
        return f"Fish fed: {len(my_aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        value = 0
        my_aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        for fish in my_aquarium.fish:
            value += fish.price

        for decoration in my_aquarium.decorations:
            value += decoration.price

        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        res = []
        for a in self.aquariums:
            res.append(str(a))

        return '\n'.join(res)

controller = Controller()
aquarium = FreshwaterAquarium('vodichko')
fish1 = FreshwaterFish('ahuid', 'vodna', 15)
fish2 = FreshwaterFish('dga', 'vodna', 15)
fish3 = SaltwaterFish('dnfioaga', 'vzenna', 12)
cvetence = Plant()
pod = Ornament()
print(controller.add_aquarium('FreshwaterAquarium', 'yiosgdf'))
print(controller.add_decoration('Plant'))
print(controller.insert_decoration('yiosgdf', 'Plant'))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_fish('yiosgdf','FreshwaterFish', 'robochko', 'vodna', 15))
print(controller.add_aquarium('gjfk', 'y'))
print(controller.feed_fish('yiosgdf'))
print(controller.calculate_value('yiosgdf'))
print(controller.report())
print(controller.insert_decoration('yiosgdf', 'pishka'))
print(controller.add_fish('yiosgdf', 'SaltwaterFish', 'dja', 'zemna', 41641))


