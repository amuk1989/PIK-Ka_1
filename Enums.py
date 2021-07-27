from enum import Enum, IntEnum


class DriverStatus(Enum):
    Success = 1
    NoAnswer = 2


class DeviceName(Enum):
    spectrum_analizer = 0
    generator = 1
    osciloscope = 2
    combinedDevice = 3
