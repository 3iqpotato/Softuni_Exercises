from project.meals.meal import Meal


class Starter(Meal):
    def __init__(self, name, price, quantity=60):
        super().__init__(name, price, quantity)

    def details(self):#TODO :.2f
        return f"Starter {self.name}: {self.price:.2f}lv/piece"

# a = Starter('koko', 13)
# print(a.details())
# print(a.quantity)