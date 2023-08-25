from python_oop.first_steps_in_oop.project001.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for p in self.pokemons:
            if p.name == pokemon_name:
                self.pokemons.remove(p)
                return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        res = ''
        for p in self.pokemons:
            res += f'- {p.pokemon_details()}\n'

        return f'Pokemon Trainer {self.name}\n'\
                f'Pokemon count {len(self.pokemons)}\n'\
                 f'{res}'
