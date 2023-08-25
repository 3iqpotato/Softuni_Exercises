from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXYGEN = 90

    def __init__(self, name):
        super().__init__(name, Meteorologist.OXYGEN)

    def breathe(self):
        self.oxygen -= 15


