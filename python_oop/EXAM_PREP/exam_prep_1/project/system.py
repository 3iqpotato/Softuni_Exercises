from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
        except IndexError:
            return "Hardware does not exist"

        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
        except IndexError:
            return "Hardware does not exist"

        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [h for h in System._software if h.name == software_name][0]
        except IndexError:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        all_software_memory = sum(s.memory_consumption for s in System._software)
        all_hardware_memory = sum(s.memory for s in System._hardware)
        capacyti_for_all_softwares = sum(s.capacity_consumption for s in System._software)
        capacyti_for_all_hardwares = sum(s.capacity for s in System._hardware)

        return f"System Analysis\n"\
                f"Hardware Components: {len(System._hardware)}\n"\
                f"Software Components: {len(System._software)}\n"\
                f"Total Operational Memory: {all_software_memory} / {all_hardware_memory}\n"\
                f"Total Capacity Taken: {capacyti_for_all_softwares} / {capacyti_for_all_hardwares}"


    @staticmethod
    def system_split():
        res = []
        for hardware in System._hardware:
            express_components = [c for c in hardware.software_components if c.software_type == 'Express']
            light_components = [c for c in hardware.software_components if c.software_type == 'Light']

            total_memory = sum(c.memory_consumption for c in hardware.software_components)
            total_capacity = sum(c.capacity_consumption  for c in hardware.software_components)

            softwares = [c.name for c in hardware.software_components]

            message = f"Hardware Component - {hardware.name}\n"\
                        f"Express Software Components: {len(express_components)}\n"\
                        f"Light Software Components: {len(light_components)}\n"\
                        f"Memory Usage: {total_memory} / {hardware.memory}\n"\
                        f"Capacity Usage: {total_capacity} / {hardware.capacity}\n"\
                        f"Type: {hardware.hardware_type}\n"\
                        f"Software Components: {', '.join(softwares) if softwares else 'None'}"

            res.append(message)
        return '\n'.join(res)

System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
print(System.analyze())
System.register_light_software("HDD", "Test", 0, 10)
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)
print(System.analyze())
System.release_software_component("SSD", "Linux")
print(System.system_split())
