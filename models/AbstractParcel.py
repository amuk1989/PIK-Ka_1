from __future__ import annotations
from abc import ABC, abstractmethod
from models.MarkerModel import marker_model
from typing import List
from floatMethods import equal

class AbstractParcel(ABC):
    _graph = {}
    _markers = []
    _observers: List[AbstractParcelObserver] = []
    _name: str

    @abstractmethod
    def add_marker(self, marker: marker_model):
        pass

    @property
    @abstractmethod
    def get_mask(self):
        pass

    def __str__(self):
        return self._name
    def get_graph(self):
        return self._graph
    def set_graph(self, value):
        self._graph = value
    def get_markers(self):
        return self._markers

    def add_marker(self, marker: marker_model):
        self._markers.append(marker)
        self.notify()
    def insert_marker(self, i:int, markers: List[marker_model]):
        self._markers = markers
        self.notify()
    def delete_marker(self, marker: marker_model):
        for i in range(0, len(self._markers)):
            if marker.x == self._markers[i].x and marker.x == self._markers[i].x:
                self._markers.pop(i)
                self.notify()

    def attach(self, observer: AbstractParcelObserver):
        self._observers.append(observer)

    def detach(self, observer: AbstractParcelObserver):
        self._observers.remove(observer)

    def notify(self):
        if len(self._observers) > 0:
            for observer in self._observers:
                observer.update(self)

class AbstractParcelObserver(ABC):
    @abstractmethod
    def update(self, subject: AbstractParcel):
        pass