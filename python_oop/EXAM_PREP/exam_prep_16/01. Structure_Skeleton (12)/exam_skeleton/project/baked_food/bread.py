from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    SIZE = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, Bread.SIZE, price)
