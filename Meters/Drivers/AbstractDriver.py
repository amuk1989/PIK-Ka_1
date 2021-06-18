from abc import ABC, abstractmethod
import pyvisa as visa


class AbstractDriver(ABC):
    # Интерфейс драйвера
    @abstractmethod
    def __init__(self):
        self._model: str

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_idn(self):
        pass

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def device_init(self, ip: str, port: str):
        return 'Драйвер не обнаружен'

    def get_model(self):
        return self._model
