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
    _observers: List[AbstractParcelObserver] = []
    __markers: List[marker_model] = []
    __detonation_time: float = 1
    _parcel_mode: int = 0

    def __init__(self):
        pass

    #@property
    def get_graph(self):
        return self.__signal

    @property
    def parcel_mode(self):
        return self._parcel_mode

    @property
    def detonation_time(self):
        return self.__detonation_time

    @parcel_mode.setter
    def parcel_mode(self,value):
        self._parcel_mode = value
        if parcel_modes[value] == 'Режим самоликвидации':
            self.detonation_time = 14000

    @detonation_time.setter
    def detonation_time(self,value):
        self.__detonation_time = value

    def attach(self, observer: AbstractParcelObserver):
        self._observers.append(observer)

    def detach(self, observer: AbstractParcelObserver):
        self._observers.remove(observer)

    def add_marker(self, marker: marker_model):
        print(f'add marker parcel {marker}')
        self.__markers.append(marker)

    def get_markers(self):
        return self.__markers

    def notify(self):
        if len(self._observers) > 0:
            for observer in self._observers:
                observer.update(self)

    def create_signal(self):
        time = self.detonation_time*1000/4096
        value ={
                49999:0, #1
                50000:0, #2
                50000.001:5,
                50000.25:5,
                50000.25:0,
                50200:0,
                50200.001:5,
                50200.25:5,
                50200.25:0,
                50200 + (time): 0,
                50200.001 + (time): 5,
                50200.25 + (time): 5,
                50200.25 + (time): 0,
                50400 + (time): 0,
                50400.001 + (time): 5,
                50400.25 + (time): 5,
                50400.25 + (time): 0,
                50401.25 + (time): 0,
                }
        self.__signal = value
        self.notify()
