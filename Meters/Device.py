from __future__ import annotations
from typing import List
from Meters.AbstractDevices import AbstractObserver
import pyvisa

class Device():
    _observers: List[AbstractObserver] = []
    def __init__(self, device: pyvisa.Resource, visa_addres: str):
        self.device = device
        data = '*RST'.encode()
        self.device.write(data.decode('utf-8'))
        propertiesList = str(self.device.query('*IDN?')).split(', ')
        self.name = propertiesList[1]
        self.ip = visa_addres.split('::')[1]
        self.isConnect = False
        #self.set_driver()

    def __get_name(self):
        return self._name
    def __set_name(self, value):
        self._name = value
    name = property(__get_name, __set_name, doc='Device name/model')

    def __get_ip(self):
        return self._ip
    def __set_ip(self, value):
        self._ip = value
    ip = property(__get_ip, __set_ip, doc='ip addres')

    def __get_state(self):
        return self._state
    def __set_state(self, value: bool):
        self._state = value
    isConnect = property(__get_state, __set_state, doc='connect status')

    def connect(self, state: bool):
        if self.isConnect != state:
            self.isConnect = state
            if state:
                print(f'{self.name} connected')
            else:
                print(f'{self.name} disconnected')
            self.notify()

    def attach(self, observer: AbstractObserver):
        self._observers.append(observer)

    def detach(self, observer: AbstractObserver):
        self._observers.remove(observer)

    def notify(self):
        if len(self._observers) > 0:
            for observer in self._observers:
                observer.update(self)

    def set_driver(self):
        return 'Не удалось подключить драйвер'