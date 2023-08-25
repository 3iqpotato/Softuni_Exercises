from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    OXYGEN = 50

    def __init__(self, name):
        super().__init__(name, Geodesist.OXYGEN)


