from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name):
        super().__init__(name, MainService.CAPACITY)

    def details(self):
        if not self.robots:
            r = 'none'
        else:
            r = ' '.join([rob.name for rob in self.robots])

        return f"{self.name} Main Service:\n" \
               f"Robots: {r}"

# a = MainService('kur', 10)
# a.robots.append(FemaleRobot('kur', 'bql', 10))
# print(a.details())