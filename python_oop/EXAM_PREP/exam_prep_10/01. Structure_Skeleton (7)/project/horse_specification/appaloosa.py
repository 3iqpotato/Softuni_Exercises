from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    @property
    def training_increase(self):
        return 2

    @property
    def max_speed(self):
        return 120


