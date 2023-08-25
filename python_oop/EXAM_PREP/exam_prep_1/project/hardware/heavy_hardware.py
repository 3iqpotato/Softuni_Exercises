from math import floor

from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory):
        m = floor(memory * 0.75)
        super().__init__(name, "Heavy", capacity * 2, m)
