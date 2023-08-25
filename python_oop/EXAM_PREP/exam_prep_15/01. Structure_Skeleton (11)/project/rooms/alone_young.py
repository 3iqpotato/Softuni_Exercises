from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, 1)
        self.calculate_expenses(*self.appliances)

    @property
    def room_cost(self):
        return 10

    @property
    def appliances(self):
        return [TV()]


# a = AloneYoung('mama', 300)
# print(a.expenses)