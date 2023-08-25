from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    @property
    @abstractmethod
    def sponsors(self):
        pass

    @property
    @abstractmethod
    def expenses_per_race(self):
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        for prices in self.sponsors.values():
            for place, money in prices.items():
                if race_pos <= place:
                    revenue += money
                    break

        revenue -= self.expenses_per_race
        self.__budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.__budget}$"



