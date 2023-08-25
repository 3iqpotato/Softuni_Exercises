from project.software.software import Software


class Hardware:
    def __init__(self, name, hardware_type: str, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if self.memory >= software.memory_consumption and self.capacity >= software.capacity_consumption:
            # self.memory -= software.memory_consumption
            # self.capacity -= software.capacity_consumption
            self.software_components.append(software)
            return
        raise Exception('Software cannot be installed')

    def uninstall(self, software: Software):
        self.software_components.remove(software)

