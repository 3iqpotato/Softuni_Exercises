# from abc import ABC, abstractmethod
from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

        self.__expenses = value

    def calculate_expenses(self, *args):
        res = 0
        for el in args:
            res += el.get_monthly_expense()

        self.expenses = res

    @property
    def room_cost(self):
        return 10
# tv = TV()
# c = Child(10)
# a = Room('kur', 10, 10)
# a.calculate_expenses(tv, c)
# print(a.expenses)
