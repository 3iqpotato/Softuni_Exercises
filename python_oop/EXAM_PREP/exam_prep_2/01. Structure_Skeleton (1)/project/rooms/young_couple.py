from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import Tv
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 20
        tv = Tv()
        fridge = Fridge()
        laptop = Laptop()
        self.appliances = [tv, tv, fridge, fridge, laptop, laptop]
        self.calculate_expenses(self.appliances)




