class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0
        self.ordered_meals = {}
    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if len(value) == 10:
            if value[0] == '0':
                if value.isdigit():
                    self.__phone_number = value
                    return
        raise ValueError("Invalid phone number!")


# a = Client('0989536373')
# print(a.phone_number)