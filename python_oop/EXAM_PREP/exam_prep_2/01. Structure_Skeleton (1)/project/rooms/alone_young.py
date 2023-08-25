from project.appliances.tv import Tv
from project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, 1)
        self.room_cost = 10
        tv = Tv()
        self.appliances = [tv]
        self.calculate_expenses(self.appliances)

