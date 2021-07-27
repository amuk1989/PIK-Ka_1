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

    def _is_measure_active_get(self) -> bool:
        return self._is_measure_active

    def _is_measure_active_set(self, value: bool):
        self._is_measure_active = value

    is_measure_active = property(_is_measure_active_get, _is_measure_active_set)

    def _measure_data_get(self) -> List[float]:
        return self._measure_data

    def _measure_data_set(self, value: List[float]):
        self._measure_data = value

    measure_data = property(_measure_data_get, _measure_data_set)

    def _x_data_get(self) -> List[float]:
        return self._x_data

    def _x_data_set(self, value: List[float]):
        self._x_data = value

    x_data = property(_x_data_get, _x_data_set)

    def __max_range_get(self) -> float:
        return self._max_range

    def __max_range_set(self, value: float):
        self._max_range = value

    max_range = property(__max_range_get, __max_range_set)

    def __min_range_get(self) -> float:
        return self._min_range

    def __min_range_set(self, value: float):
        self._min_range = value

    min_range = property(__min_range_get, __min_range_set)

    def _dots_count_range_get(self) -> int:
        return self._dots_count_range

    def _dots_count_range_set(self, value: int):
        self._dots_count_range = value

    dots_count_range = property(_dots_count_range_get, _dots_count_range_set)

    def _span_get(self) -> float:
        return self._span

    def _span_set(self, value: float):
        self._span = value

    span_range = property(_span_get, _span_set)
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
    def min_range_set(self, value: float):
        pass

    @abstractmethod
    def max_range_set(self, value: float):
        pass

    @abstractmethod
    def get_idn(self):
        pass

    @abstractmethod
    def start_device(self):
        pass

    @abstractmethod
    def get_measure_data(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def get_range(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def device_init(self, ip: str, port: str):
        return 'Драйвер не обнаружен'

    def get_model(self):
        return self._model
