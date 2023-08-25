from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    VALID_FOOD_TYPES = {
        'Bread': Bread,
        'Cake': Cake
    }

    VALID_DRINK_TYPES = {
        'Tea': Tea,
        'Water': Water
    }

    VALID_TABLE_TYPES = {
        'InsideTable': InsideTable,
        'OutsideTable': OutsideTable
    }

    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        food = self.find_food_in_food_menu_by_name(name)
        if food:
            raise Exception(f"{food_type} {name} is already in the menu!")
        try:
            f = self.VALID_FOOD_TYPES[food_type](name, price)
        except KeyError:
            return
        self.food_menu.append(f)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        drink = self.find_drink_in_drink_menu_by_name(name)
        if drink:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        try:
            d = self.VALID_DRINK_TYPES[drink_type](name, portion, brand)
        except KeyError:
            return
        self.drinks_menu.append(d)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table = self.find_table_by_table_number(table_number)
        if table:
            raise Exception(f"Table {table_number} is already in the bakery!")
        try:
            t = self.VALID_TABLE_TYPES[table_type](table_number, capacity)
        except KeyError:
            return
        self.tables_repository.append(t)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = self.find_table_to_reserve(number_of_people)
        if table:
            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        table = self.find_table_by_table_number(table_number)
        if not table:
            return f"Could not find table {table_number}"

        res = []
        food_not_in_menu = []
        res.append(f"Table {table_number} ordered:")
        for food_name in args:
            food = self.find_food_in_food_menu_by_name(food_name)
            if food:
                table.food_orders.append(food)
                res.append(food.__repr__())
            else:
                food_not_in_menu.append(food_name)
        res.append(f'{self.name} does not have in the menu:')
        for food_name in food_not_in_menu:
            res.append(food_name)

        return '\n'.join(res)

    def order_drink(self, table_number: int, *args):
        table = self.find_table_by_table_number(table_number)
        if not table:
            return f"Could not find table {table_number}"
        res = []
        drinks_not_in_menu = []
        res.append(f"Table {table_number} ordered:")
        for drink_name in args:
            drink = self.find_drink_in_drink_menu_by_name(drink_name)
            if drink:
                table.drink_orders.append(drink)
                res.append(drink.__repr__())
            else:
                drinks_not_in_menu.append(drink_name)
        res.append(f'{self.name} does not have in the menu:')
        for drink_name in drinks_not_in_menu:
            res.append(drink_name)

        return '\n'.join(res)

    def leave_table(self, table_number: int):
        table = self.find_table_by_table_number(table_number)
        bill = table.get_bill()
        table.clear()
        self.total_income += bill
        return f"Table: {table_number}\n"\
                f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        res = []
        for t in self.tables_repository:
            r = t.free_table_info()
            if r:
                res.append(r)
        return '\n'.join(res)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def find_food_in_food_menu_by_name(self, name):
        for food in self.food_menu:
            if food.name == name:
                return food

    def find_drink_in_drink_menu_by_name(self, name):
        for drink in self.drinks_menu:
            if drink.name == name:
                return drink

    def find_table_by_table_number(self, number):
        for table in self.tables_repository:
            if table.table_number == number:
                return table

    def find_table_to_reserve(self, num_people):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= num_people:
                return table



# a = Bakery('mama')
# print(a.add_food('Bread', 'hlqb', 10))
# print(a.add_drink('Tea', 'cheren', 300, 'gorski'))
# print(a.add_table('InsideTable', 10, 10))
# print(a.add_table('InsideTable', 11, 10))
# print(a.add_table('InsideTable', 12, 10))
# print(a.reserve_table(3))
# print(a.get_free_tables_info())
# print(a.leave_table(10))
# print(a.order_food(10, 'kur', 'hlqb', 'kiko'))
# print(a.order_drink(10, 'pisja', 'cheren', 'loli'))