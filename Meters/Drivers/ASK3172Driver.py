from typing import List

from Enums import DeviceName
from Meters.Drivers.AbstractDriver import AbstractDriver


class ASK3172Driver(AbstractDriver):
    def __init__(self):
        self.name = DeviceName.osciloscope

    def __str__(self):
        return 'Осцилограф АСК-3172'

    def min_range_set(self, value: float):
        pass

    def max_range_set(self, value: float):
        pass

    def get_idn(self):
        pass

    def start(self):
        pass

    def close(self):
        pass

    def get_measure_data(self):
        pass

    def start_device(self):
        pass

    def stop(self):
        pass

    def get_range(self):
        pass

    def set_range(self, start: float, value: float, dots_count: int):
        pass

    def set_min_range(self, value: float):
        pass

    def set_max_range(self, value: float):
        pass
