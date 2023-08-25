from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.calculate_expenses(*self.appliances)

    @property
    def room_cost(self):
        return 20

    @property
    def appliances(self):
        return [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]

# a = YoungCouple('ma', 100, 100)
# print(a.expenses)