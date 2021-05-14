from __future__ import annotations
from abc import ABC, abstractmethod
from models.MarkerModel import marker_model

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

    @abstractmethod
    def add_marker(self, marker: marker_model):
        pass

    @abstractmethod
    def get_markers(self):
        pass

    @property
    @abstractmethod
    def set_graph(self):
        pass

class AbstractParcelObserver(ABC):
    @abstractmethod
    def update(self, subject: AbstractParcel):
        pass