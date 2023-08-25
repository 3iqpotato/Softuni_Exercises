class Room:
    def __init__(self, family_name: str, budget, members_count):
        self.family_name = family_name
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
        total_sum = 0
        for el in args:
            for appliance_and_child in el:
                total_sum += appliance_and_child.get_monthly_expense()

        self.expenses = total_sum
        if self.expenses < 0:
            raise ValueError("Expenses cannot be negative")


