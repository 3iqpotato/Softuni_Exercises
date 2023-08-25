from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXYGEN = 70

    def __init__(self, name):
        super().__init__(name, Biologist.OXYGEN)

    def breathe(self):
        self.oxygen -= 5
