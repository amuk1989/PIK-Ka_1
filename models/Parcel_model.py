from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


parcel_modes = [
    'Режим программирования',
    'Режим контактного датчика',
    'Режим самоликвидации',
]

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

class AbstractParcel(ABC):
    @abstractmethod
    def attach(self, observer: AbstractParcelObserver):
        pass
    @abstractmethod
    def detach(self, observer: AbstractParcelObserver):
        pass
    @abstractmethod
    def notify(self):
        pass

class AbstractParcelObserver(ABC):
    @abstractmethod
    def update(self, subject: AbstractParcel):
        pass

@singleton
class Parcel(AbstractParcel):
    __detonation_time = 2
    __parcel_mode = 2

    observers: List[AbstractParcelObserver] = []

    @property
    def signal(self):
        return self.__signal

    @property
    def parcel_mode(self):
        return self.__parcel_mode

    @property
    def detonation_time(self):
        return self.__detonation_time

    @parcel_mode.setter
    def parcel_mode(self,value):
        self.__parcel_mode = value
        if parcel_modes[value] == 'Режим самоликвидации':
            self.detonation_time = 14000

    @detonation_time.setter
    def detonation_time(self,value):
        self.__detonation_time = value
        self.__create_signal()
        self.notify()

    def __init__(self):
        self.__create_signal()

    def attach(self, observer: AbstractParcelObserver):
        self._observers.append(observer)

    def detach(self, observer: AbstractParcelObserver):
        self._observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def __create_signal(self):
        time = self.detonation_time*1000/4096
        print(int(self.detonation_time))
        value ={
                49999:0,
                50000:0,
                50000.001:5,
                50000.25:5,
                50000.25:0,
                50200:0,
                50200.001:5,
                50200.25:5,
                50200.25:0,
                50200+(time):0,
                50200+(time)+0.25:0,
                }
        self.__signal = value
        self.notify()

class ParcelObserver(AbstractParcelObserver):
    def update(self, subject: AbstractParcel):
        mainWindow.parcelWidget.drawAmp
