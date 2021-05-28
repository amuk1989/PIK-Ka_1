#from __future__ import annotations
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

    def __init__(self, time:float = 0.1, mode: int = 0, duration: int = 200, count: int = 10000,
                 max_power = 1.5, min_power = 0.1, step = 0.1):
        self.__detonation_time: float = time
        self._parcel_mode: int = mode
        self.__signal_duration: int = duration
        self.__parcel_count: int = count
        self.__max_power: float = max_power
        self.__min_power: float = min_power
        self.__step_power: float = step
        self._name = 'Parcel'

    def get_mask(self):
        return 'Маркер №, X, Y'

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
            self.detonation_time = 14000

    @signal_duration.setter
    def signal_duration(self,value):
        self.__signal_duration = value

    @detonation_time.setter
    def detonation_time(self,value):
        self.__detonation_time = value

    def create_signal(self):
        time = self.detonation_time*1000/4096
        signal_duration = self.__signal_duration/1000
        value ={
                49999:0, #1
                50000:0, #2
                50000.001:5,
                50000 + signal_duration:5,
                50000 + signal_duration:0,
                50200:0,
                50200.001:5,
                50200. + signal_duration:5,
                50200. + signal_duration:0,
                50200 + (time): 0,
                50200.001 + (time): 5,
                50200. + signal_duration + (time): 5,
                50200. + signal_duration + (time): 0,
                50400 + (time): 0,
                50400.001 + (time): 5,
                50400. + signal_duration + (time): 5,
                50400. + signal_duration + (time): 0,
                50401. + signal_duration + (time): 0,
                }
        self.set_graph(value)
        self.notify()

    def create_from_file(self, graph: dict):
        self.set_graph(graph)
        self.notify()