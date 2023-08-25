from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    max_mileage = 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, CargoVan.max_mileage)

    def drive(self, mileage: float):
        percent = (mileage / self.max_mileage) * 100
        percent = round(percent)
        self.battery_level -= (percent + 5)


# a = CargoVan('passat', 'lada', '7361')
# a.drive(180)
# print(a.battery_level)