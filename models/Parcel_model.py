import math
from bitarray import bitarray, util
from models.AbstractParcel import AbstractParcelObserver,AbstractParcel
from typing import List
from models.singelton import singleton
from models.MarkerModel import marker_model

parcel_modes = [
    'Режим программирования',
    'Режим контактного датчика',
    'Режим самоликвидации',
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

    def __init__(self, time:float = 1, mode: int = 0, duration: int = 200, count: int = 1,
                 max_power = 1.5, min_power = 0.1, step = 0.1):
        self.__detonation_time: float = time
        self._parcel_mode: int = mode
        self.__signal_duration: int = duration
        self.__parcel_count: int = count
        self.__max_power: float = max_power
        self.__min_power: float = min_power
        self.__step_power: float = step
        self._name = 'Parcel'
        self.bit_parcel = bitarray()

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
        self.__min_power = min_value
        self.__max_power = max_value
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
    def parcel_mode(self,value):
        self._parcel_mode = value
        if parcel_modes[value] == 'Режим самоликвидации':
            self.detonation_time = 4095

    @signal_duration.setter
    def signal_duration(self,value):
        self.__signal_duration = value

    @detonation_time.setter
    def detonation_time(self,value):
        self.__detonation_time = value

    def create_signal(self, symbol_rate = 9600,bytes_count = 2):
        time = int(self.__detonation_time)

        signal_rate = int((1/symbol_rate)*(10**6))
        self.bit_parcel.clear()
        self.bit_parcel = util.int2ba(time, length=bytes_count * 8 - 4)
        for i in range(0, 4):
            self.bit_parcel.insert(i, (self.bit_parcel[i] ^ self.bit_parcel[i + 4] ^ self.bit_parcel[i + 8]))

        uart_bits = {}

        uart_bits[0] = 0
        for i in range(0, bytes_count * 8):
            if i < 8:
                uart_bits[i+1] = self.bit_parcel[i]
            elif i == 8:
                uart_bits[i+1] = 1
                uart_bits[i+2] = 0
                uart_bits[i+3] = self.bit_parcel[i]
            elif i < 16:
                uart_bits[i+3] = self.bit_parcel[i]
        uart_bits[19] = 1

        value = {}
        for i in range(0, signal_rate * len(uart_bits)):
            value[i] = uart_bits[math.floor(i/signal_rate)]
        self.set_graph(value)
        self.notify()

    def create_from_file(self, graph: dict):
        self.set_graph(graph)
        self.notify()
