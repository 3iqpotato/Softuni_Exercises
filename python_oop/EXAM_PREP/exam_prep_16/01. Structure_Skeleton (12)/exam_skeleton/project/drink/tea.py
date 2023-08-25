from project.drink.drink import Drink


class Tea(Drink):
    COST = 2.5

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, Tea.COST, brand)