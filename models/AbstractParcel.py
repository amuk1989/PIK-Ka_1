from __future__ import annotations
from abc import ABC, abstractmethod

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

    @property
    @abstractmethod
    def set_graph(self):
        pass

    @property
    @abstractmethod
    def detonation_time(self):
        pass

class AbstractParcelObserver(ABC):
    @abstractmethod
    def update(self, subject: AbstractParcel):
        pass