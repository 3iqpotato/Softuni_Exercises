from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    receipt_id = 1
    VALID_MEALS_TYPES = {
        'Starter': Starter,
        'MainDish': MainDish,
        'Dessert': Dessert
    }

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        if self.check_if_client_exists(client_phone_number):
            raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.VALID_MEALS_TYPES:
                self.menu.append(meal)

    def show_menu(self):
        if self.check_if_menu_is_ready():

            res = []
            for meal in self.menu:
                res.append(meal.details())

            return '\n'.join(res)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):#TODO :.2f
        if self.check_if_menu_is_ready():
            if not self.check_if_client_exists(client_phone_number):
                self.register_client(client_phone_number)

        client = self.find_client_by_phone_number(client_phone_number)

        meals_ordered = {}
        current_bill = 0
        for meal_name, quantity in meal_names_and_quantities.items():#TODO add to cclient_cart_and_reduce_meals_quantity
            meal = self.find_meal_in_menu(meal_name)
            if meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

            if meal in meals_ordered:
                meals_ordered[meal] += quantity
            else:
                meals_ordered[meal] = quantity

            current_bill += quantity * meal.price

        client.bill += current_bill

        if not client.ordered_meals:
            client.ordered_meals = meals_ordered
        else:
            for m, q in meals_ordered.items():
                if m in client.ordered_meals:
                    client.ordered_meals[m] += q
                else:
                    client.ordered_meals[m] = q

        for m in meals_ordered:
            client.shopping_cart.append(m)
            m.quantity -= meals_ordered[m]

        return f"Client {client_phone_number} successfully ordered {', '.join(m.name for m in client.shopping_cart)} for {client.bill:.2f}lv."


    def cancel_order(self, client_phone_number: str):
        client = self.find_client_by_phone_number(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for m, q in client.ordered_meals.items():
            m.quantity += q

        client.ordered_meals = {}
        client.shopping_cart = []
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.find_client_by_phone_number(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        client.shopping_cart = []
        client.ordered_meals = {}
        m = client.bill
        client.bill = 0

        r = self.receipt_id
        self.receipt_id += 1

        return f"Receipt #{r} with total amount of {m:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f'Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients.'

    def check_if_client_exists(self, client_num):
        for c in self.clients_list:
            if c.phone_number == client_num:
                return True
        return False

    def check_if_menu_is_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        return True

    def find_meal_in_menu(self, meal_name):
        for m in self.menu:
            if m.name == meal_name:
                return m
        raise Exception(f"{meal_name} is not on the menu!")

    def find_client_by_phone_number(self, number):
        return [c for c in self.clients_list if c.phone_number == number][0]
# a = FoodOrdersApp()
# # print(a.register_client('0909090909'))
# print(a.register_client('0909090909'))