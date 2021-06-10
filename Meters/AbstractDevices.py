from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, subject: AbstractDevices):
        pass

class AbstractDevices(ABC):
    _observers: List[AbstractObserver] = []

    def attach(self, observer: AbstractObserver):
        self._observers.append(observer)

    def detach(self, observer: AbstractObserver):
        self._observers.remove(observer)

    def __get_name(self):
        return self._name
    def __set_name(self, value):
        self._name = value
        #self.notify()
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
