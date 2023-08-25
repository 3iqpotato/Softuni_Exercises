from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import Tv
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one+pension_two, 2)
        self.room_cost = 15
        tv = Tv()
        fridge = Fridge()
        stove = Stove()
        self.appliances = [tv, tv, fridge, fridge, stove, stove]
        self.calculate_expenses(self.appliances)

