from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []


    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        users_id_nums = [u.driving_license_number for u in self.users]
        if driving_license_number in users_id_nums:
            return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):

        if vehicle_type == 'PassengerCar':
            license_nums = [v.license_plate_number for v in self.vehicles]

            if license_plate_number in license_nums:
                return f"{license_plate_number} belongs to another vehicle."

            vehicle = PassengerCar(brand, model, license_plate_number)
            self.vehicles.append(vehicle)

            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

        elif vehicle_type == 'CargoVan':
            license_nums = [v.license_plate_number for v in self.vehicles]

            if license_plate_number in license_nums:
                return f"{license_plate_number} belongs to another vehicle."

            vehicle = CargoVan(brand, model, license_plate_number)
            self.vehicles.append(vehicle)

            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

        return f"Vehicle type {vehicle_type} is inaccessible."

    def allow_route(self, start_point: str, end_point: str, length: float):
        id_num = len(self.routes) + 1

        for rout in self.routes:
            if rout.start_point == start_point and rout.end_point == end_point and rout.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            if rout.start_point == start_point and rout.end_point == end_point and rout.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            if rout.start_point == start_point and rout.end_point == end_point and rout.length > length:
                rout.is_locked = True

        new_route = Route(start_point, end_point, length, id_num)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle = [u for u in self.vehicles if u.license_plate_number == license_plate_number][0]

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = [r for r in self.routes if r.route_id == route_id][0]

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()

        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        vehicles_for_repair = [v for v in self.vehicles if v.is_damaged]
        sorted_vehicles = sorted(vehicles_for_repair, key=lambda vehicle: (vehicle.brand, vehicle.model))

        num_repaired = 0
        for idx in range(count):
            if len(sorted_vehicles) > idx:
                sorted_vehicles[idx].change_status()
                sorted_vehicles[idx].recharge()
                num_repaired += 1
            else:
                break
        return f"{num_repaired} vehicles were successfully repaired!"

    def users_report(self):
        users = sorted(self.users, key=lambda user: -user.rating)
        res = ["*** E-Drive-Rent ***"]
        res.append(('\n'.join(str(user) for user in users)))
        return '\n'.join(res)





