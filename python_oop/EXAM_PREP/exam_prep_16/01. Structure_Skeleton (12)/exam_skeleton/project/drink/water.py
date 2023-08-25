from project.drink.drink import Drink


class Water(Drink):
    COST = 1.5

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, Water.COST, brand)