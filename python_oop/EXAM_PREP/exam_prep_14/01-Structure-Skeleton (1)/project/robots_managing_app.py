from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = {
        'SecondaryService': SecondaryService,
        'MainService': MainService
    }

    VALID_ROBOT_TYPES = {
        'MaleRobot': MaleRobot,
        'FemaleRobot': FemaleRobot
    }

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE_TYPES:
            raise Exception("Invalid service type!")

        service = self.VALID_SERVICE_TYPES[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        try:
            robot = self.VALID_ROBOT_TYPES[robot_type](name, kind, price)
        except KeyError:
            raise Exception("Invalid robot type!")

        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.find_robot_by_name(robot_name)
        service = self.find_service_by_name(service_name)

        if self.check_if_robot_is_suitable(robot, service): #TODO dali se namalqva capacityto
            if len(service.robots) < service.capacity:
                self.robots.remove(robot)
                service.robots.append(robot)
                # service.capacity -= 1
                return f"Successfully added {robot_name} to {service_name}."

            raise Exception("Not enough capacity for this robot!")

        return "Unsuitable service."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.find_service_by_name(service_name)
        robot = self.check_if_robot_in_service(service, robot_name)

        if robot:
            service.robots.remove(robot) #TODO pak capacityto
            # service.capacity += 1
            self.robots.append(robot)
            return f"Successfully removed {robot_name} from {service_name}."

        raise Exception("No such robot in this service!")

    def feed_all_robots_from_service(self, service_name: str):
        service = self.find_service_by_name(service_name)
        count = 0
        for robot in service.robots:
            count += 1
            robot.eating()
        return f"Robots fed: {count}."

    def service_price(self, service_name: str):
        service = self.find_service_by_name(service_name)
        price = sum(r.price for r in service.robots)
        return f"The value of service {service_name} is {price:.2f}."

    def __str__(self):
        res = []
        for service in self.services:
            res.append(service.details())

        return '\n'.join(res)

    def find_robot_by_name(self, name):
        for robot in self.robots:
            if robot.name == name:
                return robot

    def find_service_by_name(self, name):
        for service in self.services:
            if service.name == name:
                return service

    @staticmethod
    def check_if_robot_is_suitable(robot, service):
        if robot.__class__.__name__ == 'FemaleRobot' and service.__class__.__name__ == 'SecondaryService':
            return True

        if robot.__class__.__name__ == 'MaleRobot' and service.__class__.__name__ == 'MainService':
            return True
        return False

    @staticmethod
    def check_if_robot_in_service(service, robot_name):
        for robot in service.robots:
            if robot.name == robot_name:
                return robot

a = RobotsManagingApp()
print(a.add_service('MainService', 'kur'))
print(a.add_robot('MaleRobot', 'kur', 'bql', 10))
print(a.add_robot('MaleRobot', 'kur1', 'bql', 10))
print(a.add_robot_to_service('kur', 'kur'))
print(a.add_robot_to_service('kur1', 'kur'))
print(a.remove_robot_from_service('kur', 'kur'))
print(a.feed_all_robots_from_service('kur'))
print(a.service_price('kur'))
print(a)