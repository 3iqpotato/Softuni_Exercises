from math import floor

from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        c = floor(capacity * 0.25)
        m = floor(memory * 1.75)
        super().__init__(name, "Power", c, m)