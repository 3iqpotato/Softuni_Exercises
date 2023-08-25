class Player:
    player_names = [] #TODO ako se maha igrach trqbva i imeto mu da se mahne ot tuk
    max_stamina_value = 100

    def __init__(self, name, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':  # TODO moze da ne iska strip
            raise ValueError("Name not valid!")

        if value in self.player_names:
            raise Exception(f"Name {value} is already used!")

        self.player_names.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")

        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if 0 > value or value > 100:
            raise ValueError("Stamina not valid!")

        self.__stamina = value

    @property
    def need_sustenance(self):
        return 100 > self.__stamina

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

    def reduce_stamina(self):
        reduce = self.age * 2
        if self.stamina - reduce < 0:
            self.stamina = 0
        else:
            self.stamina -= reduce
#
# a = Player('loko', 18)
# a.reduce_stamina()
# print(a.stamina)