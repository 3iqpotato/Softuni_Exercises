from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one + salary_two, 2 + len(children))
        self.children = [*children]
        self.calculate_expenses(*self.appliances, *children)

    @property
    def room_cost(self):
        return 30

    @property
    def appliances(self):
        return [TV(), Fridge(), Laptop()] * self.members_count

# c1 = Child(10, 10, 10)
# c2 = Child(10, 10, 10)
# a = YoungCoupleWithChildren('peepvi', 100, 100, c1)
# print(a.expenses)
# print(a.children)