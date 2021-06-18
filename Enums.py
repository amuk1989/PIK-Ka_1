from enum import Enum


class DriverStatus(Enum):
    Success = 1
    NoAnswer = 2

class DeviceName(Enum):
    SpectrumAnalizer = 0
    Generator = 1
    Osciloscope = 2
