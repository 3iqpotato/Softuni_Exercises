from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    max_mileage = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, PassengerCar.max_mileage)

    def drive(self, mileage: float):
        percent = (mileage / self.max_mileage) * 100
        percent = round(percent)
        self.battery_level -= percent

# a = PassengerCar('passat', 'lada', '7361')
# a.drive(400)
# print(a.battery_level)