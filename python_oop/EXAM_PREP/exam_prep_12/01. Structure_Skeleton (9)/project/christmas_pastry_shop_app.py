from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_TYPES = {
        'Gingerbread': Gingerbread,
        'Stolen': Stolen
    }
    BOOTH_TYPES = {
        'Open Booth': OpenBooth,
        'Private Booth': PrivateBooth
    }

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self.check_if_delicacy_exists(name):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        delicacy = self.DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self.check_if_booth_exists(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth = self.find_booth_to_reserve(number_of_people)
        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.find_booth_by_number(booth_number)
        delicacy = self.find_delicacy_by_name(delicacy_name)
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.find_booth_by_number(booth_number)
        bill = booth.price_for_reservation
        for order in booth.delicacy_orders:
            bill += order.price

        self.income += bill
        booth.is_reserved = False
        booth.delicacy_orders = []
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\n"\
                f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def check_if_delicacy_exists(self, name):
        for d in self.delicacies:
            if d.name == name:
                return True
        return False

    def check_if_booth_exists(self, booth_num):
        for b in self.booths:
            if b.booth_number == booth_num:
                return True
        return False

    def find_booth_to_reserve(self, people):
        for b in self.booths:
            if not b.is_reserved and b.capacity >= people:
                return b
        raise Exception(f"No available booth for {people} people!")

    def find_booth_by_number(self, number):
        for b in self.booths:
            if b.booth_number == number:
                return b
        raise Exception(f"Could not find booth {number}!")

    def find_delicacy_by_name(self, name):
        for d in self.delicacies:
            if d.name == name:
                return d
        raise Exception(f"No {name} in the pastry shop!")
# a = ChristmasPastryShopApp()
# print(a.add_delicacy('Stolen', 'boza', 10))
# print(a.add_booth('Open Booth', 99, 10))
# print(a.reserve_booth(10))
# print(a.order_delicacy(99, 'boza'))
# print(a.leave_booth(99))
# shop = ChristmasPastryShopApp()
# print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
# print(shop.delicacies[0].details())
# print(shop.add_booth("Open Booth", 1, 30))
# print(shop.add_booth("Private Booth", 10, 5))
# print(shop.reserve_booth(30))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.reserve_booth(5))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.get_income())
