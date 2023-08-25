from math import floor
from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption: int, memory_consumption: int):
        capacity = floor(capacity_consumption * 1.5)
        memory = floor(memory_consumption * 0.5)
        super().__init__(name, "Light", capacity, memory)