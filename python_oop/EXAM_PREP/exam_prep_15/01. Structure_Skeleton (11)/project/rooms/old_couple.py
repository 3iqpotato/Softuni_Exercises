from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one + pension_two, 2)
        self.calculate_expenses(*self.appliances)

    @property
    def room_cost(self):
        return 15

    @property
    def appliances(self):
        return [TV(), TV(), Fridge(), Fridge(), Stove(), Stove()]

# a = OldCouple('meapj', 100, 100)
# print(a.expenses)
