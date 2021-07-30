from abc import ABC, abstractmethod
from typing import List, Tuple
import pyvisa as visa

from Enums import DeviceName


class AbstractDriver(ABC):
    # Интерфейс драйвера

    # region properties
    def _name_get(self) -> DeviceName:
        return self._name

    def _name_set(self, value: DeviceName):
        self._name = value

    name = property(_name_get, _name_set)

    def _ip_get(self) -> str:
        return self._ip

    def _ip_set(self, value: str):
        self._ip = value

    ip = property(_ip_get, _ip_set)

    def _port_get(self) -> str:
        return self._port

    def _port_set(self, value: str):
        self._port = value

    port = property(_port_get, _port_set)

    def _is_measure_active_get(self) -> bool:
        return self._is_measure_active

    def _is_measure_active_set(self, value: bool):
        self._is_measure_active = value

    is_measure_active = property(_is_measure_active_get, _is_measure_active_set)

    # endregion

    power: float = 0

    @abstractmethod
    def __init__(self):
        self._model: str
        self.name: DeviceName

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_idn(self):
        pass

    @abstractmethod
    def start_device(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def connect(self, ip: str, port: str):
        return 'Драйвер не обнаружен'

    def get_model(self):
        return self._model
