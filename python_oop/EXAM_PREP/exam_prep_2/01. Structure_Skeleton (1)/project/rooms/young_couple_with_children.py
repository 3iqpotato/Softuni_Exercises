from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import Tv
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one+salary_two, 2+len(children))
        self.room_cost = 30
        self.children = children
        self.appliances = []
        tv = Tv()
        fridge = Fridge()
        laptop = Laptop()
        for _ in range(self.members_count):
            self.appliances.extend([laptop, tv, fridge])
        self.calculate_expenses([*children, *self.appliances])

