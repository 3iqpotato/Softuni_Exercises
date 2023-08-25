from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args: Player):
        names = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                names.append(player.name)

        return f"Successfully added: {', '.join(names)}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.find_player_by_name(player_name)

        if not player:
            return None

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        if sustenance_type not in ['Food', 'Drink']:
            return None

        sustenance = self.find_supplies_by_type(sustenance_type)

        if player.stamina + sustenance.energy > 100:
            player.stamina = 100

        else:
            player.stamina += sustenance.energy

        return f"{player_name} sustained successfully with {sustenance.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_1 = self.find_player_by_name(first_player_name)
        player_2 = self.find_player_by_name(second_player_name)

        res = []
        if player_1.stamina == 0:
            res.append(f"Player {player_1.name} does not have enough stamina.")

        if player_2.stamina == 0:
            res.append(f"Player {player_2.name} does not have enough stamina.")

        if res:
            return '\n'.join(res)

        return self.dueling(player_1, player_2)

    def next_day(self):
        for player in self.players:
            player.reduce_stamina()

            self.sustain(player.name, 'Food')
            # food = [f for f in self.supplies if f.__class__.__name__ == 'Food'].pop(0)
            # player.stamina += food.energy
            # self.supplies.remove(food)

            # drink = [f for f in self.supplies if f.__class__.__name__ == 'Drink'].pop(0)
            # player.stamina += drink.energy
            # self.supplies.remove(drink)
            self.sustain(player.name, 'Drink')

    def __str__(self):
        res = []
        for player in self.players:
            res.append(str(player))

        for s in self.supplies:
            res.append(s.details())

        return '\n'.join(res)

    def find_player_by_name(self, name):
        player = [p for p in self.players if p.name == name]

        if not player:
            return None

        return player[0]

    def find_supplies_by_type(self, food_type) -> Supply: #TODO poslednata hrana
        if food_type in ['Food', 'Drink']:
            if food_type == 'Food':
                foods = [f for f in self.supplies if f.__class__.__name__ == food_type]

                if not foods:
                    raise Exception("There are no food supplies left!")

                food = foods[-1]
                self.supplies.reverse()
                food_idx = self.supplies.index(food)
                self.supplies.pop(food_idx)
                self.supplies.reverse()
                return food

            if food_type == 'Drink':
                foods = [f for f in self.supplies if f.__class__.__name__ == food_type]

                if not foods:
                    raise Exception("There are no drink supplies left!")

                food = foods[-1]
                self.supplies.reverse()
                food_idx = self.supplies.index(food)
                self.supplies.pop(food_idx)
                self.supplies.reverse()
                return food

        return None

    def dueling(self, p1, p2):
        if p1.stamina < p2.stamina:
            attack_power = p1.stamina / 2
            if p2.stamina - attack_power < 0:
                p2.stamina = 0
                return f"Winner: {p1.name}"
            p2.stamina -= attack_power
            attack2 = p2.stamina / 2
            if p1.stamina - attack2 < 0:
                p1.stamina = 0
                return f"Winner: {p2.name}"
            p1.stamina -= attack2

        elif p2.stamina < p1.stamina:
            attack_power = p2.stamina / 2
            if p1.stamina - attack_power < 0:
                p1.stamina = 0
                return f"Winner: {p2.name}"
            p1.stamina -= attack_power
            attack2 = p1.stamina / 2
            if p2.stamina - attack2 < 0:
                p2.stamina = 0
                return f"Winner: {p1.name}"
            p2.stamina -= attack2


        if p1.stamina > p2.stamina:
            return f"Winner: {p1.name}"
        else:
            return f"Winner: {p2.name}"


#
# a = Player('da', 13, 90)
# c = Player('dada', 13, 89)
# b = Controller()
# m = Drink('kokakola')
# mg = Drink('kokakola')
# f = Food('qbulka')
# fg = Food('qbulka')
# print(b.add_player(a, c))
# b.add_supply(m, mg, f, fg)
# b.next_day()
# a= 0