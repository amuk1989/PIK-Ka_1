import math
from bitarray import bitarray, util
from models.AbstractParcel import AbstractParcelObserver, AbstractParcel
from typing import List
from models.singelton import singleton
from models.MarkerModel import marker_model

parcel_modes = [
    'Режим программирования',
]


@singleton
class Parcel(AbstractParcel):
    _graph = {}
    _observers: List[AbstractParcelObserver] = []
    _markers: List[marker_model] = []
    __detonation_time: float
    _parcel_mode: int
    __signal_duration: int
    __parcel_count: int
    __max_power: float
    __min_power: float
    __step_power: float
    _name = ''

    def __init__(self, time: float = 1, mode: int = 0, duration: int = 9600, count: int = 100,
                 max_power=15.0, min_power=5.0, step=0.1, frequency=34.0):
        self.frequency: float = frequency
        self.__detonation_time: float = time
        self._parcel_mode: int = mode
        self.__signal_duration: int = duration
        self.__parcel_count: int = count
        self.__max_power: float = max_power
        self.__min_power: float = min_power
        self.__step_power: float = step
        self._name = 'Parcel'
        self.bit_parcel = bitarray()
        self.uart_bits: int = {}

    def __str__(self):
        return self._name

    def get_mask(self):
        return 'Маркер №, X, Y'

    def get_label(self):
        return 'Время, мкс', 'Value'

    def get_parcel_count(self):
        return self.__parcel_count

    def set_parcel_count(self, value):
        self.__parcel_count = value

    signal_count = property(get_parcel_count, set_parcel_count)

    def get_power(self):
        return self.__max_power, self.__min_power, self.__step_power

    def set_power(self, max_value: float, min_value: float, step: float):
        self.__max_power = max_value
        self.__min_power = min_value
        self.__step_power = step

    power = property(get_power, set_power)

    @property
    def parcel_mode(self):
        return self._parcel_mode

    @property
    def signal_duration(self):
        return self.__signal_duration

    @property
    def detonation_time(self):
        return self.__detonation_time

    @parcel_mode.setter
    def parcel_mode(self, value):
        self._parcel_mode = value
        if parcel_modes[value] == 'Режим самоликвидации':
            self.detonation_time = 4095

    @signal_duration.setter
    def signal_duration(self, value):
        self.__signal_duration = value

    @detonation_time.setter
    def detonation_time(self, value):
        self.__detonation_time = value

    def create_signal(self, bytes_count=3, control_bits=8):
        k = 0
        time = int(self.__detonation_time)
        signal_rate = int((1 / self.__signal_duration) * (10 ** 6))
        self.bit_parcel.clear()
        self.bit_parcel = util.int2ba(time, length=(bytes_count - 1) * 8)

        self.uart_bits[0] = 0

        for i in range(0, bytes_count):
            for j in range(0, 10):
                if j == 0:
                    self.uart_bits[i * 10] = 0
                elif j == 9:
                    self.uart_bits[(i * 10) + 9] = 1
                else:
                    if i == 0:
                        self.uart_bits[j] = 0
                    else:
                        self.uart_bits[j + (i * 8) + (2 * i)] = self.bit_parcel[k]
                        k += 1
        value = {}
        self.__set_crc()
        for i in range(0, signal_rate * len(self.uart_bits)):
            value[i] = (self.uart_bits[math.floor(i / signal_rate)] * (-24)) + 12
        self.set_graph(value)
        self.notify()

    def create_from_file(self, graph: dict):
        self.set_graph(graph)
        self.notify()

    def __set_crc(self):
        crc: int = 0
        crc2: int = 0
        crc_array = [
            0, 94, 188, 226, 97, 63, 221, 131, 194, 156, 126, 32, 163, 253, 31, 65,
            157, 195, 33, 127, 252, 162, 64, 30, 95, 1, 227, 189, 62, 96, 130, 220,
            35, 125, 159, 193, 66, 28, 254, 160, 225, 191, 93, 3, 128, 222, 60, 98,
            190, 224, 2, 92, 223, 129, 99, 61, 124, 34, 192, 158, 29, 67, 161, 255,
            70, 24, 250, 164, 39, 121, 155, 197, 132, 218, 56, 102, 229, 187, 89, 7,
            219, 133, 103, 57, 186, 228, 6, 88, 25, 71, 165, 251, 120, 38, 196, 154,
            101, 59, 217, 135, 4, 90, 184, 230, 167, 249, 27, 69, 198, 152, 122, 36,
            248, 166, 68, 26, 153, 199, 37, 123, 58, 100, 134, 216, 91, 5, 231, 185,
            140, 210, 48, 110, 237, 179, 81, 15, 78, 16, 242, 172, 47, 113, 147, 205,
            17, 79, 173, 243, 112, 46, 204, 146, 211, 141, 111, 49, 178, 236, 14, 80,
            175, 241, 19, 77, 206, 144, 114, 44, 109, 51, 209, 143, 12, 82, 176, 238,
            50, 108, 142, 208, 83, 13, 239, 177, 240, 174, 76, 18, 145, 207, 45, 115,
            202, 148, 118, 40, 171, 245, 23, 73, 8, 86, 180, 234, 105, 55, 213, 139,
            87, 9, 235, 181, 54, 104, 138, 212, 149, 203, 41, 119, 244, 170, 72, 22,
            233, 183, 85, 11, 136, 214, 52, 106, 43, 117, 151, 201, 74, 20, 246, 168,
            116, 42, 200, 150, 21, 75, 169, 247, 182, 232, 10, 84, 215, 137, 107, 53
        ]
        for i in range(11, 19):
            crc += self.uart_bits[i] * (2 ** (18-i))

        for i in range(21, 29):
            crc2 += self.uart_bits[i] * (2 ** (28-i))

        result = util.int2ba(crc_array[crc_array[crc] ^ crc2], length=8)

        for i in range(0, len(result)):
            self.uart_bits[i+1] = result[i]
