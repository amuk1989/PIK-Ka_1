from models.AbstractParcel import AbstractParcelObserver,AbstractParcel
from typing import List
from models.singelton import singleton
from math import sin
from models.MarkerModel import marker_model
from random import randint

@singleton
class InputSignalModel(AbstractParcel):
    #region private variables
    __signal = {}
    _observers: List[AbstractParcelObserver] = []
    __markers: List[marker_model] = []
    #endregion

    #region properties

    #region getters
    def get_graph(self):
        return self.__signal
    def get_mask(self):
        return 'Маркер №, A, Ч'
    #endregion

    #endregion

    #region Methods
    def __init__(self):
        self.create_signal()

    def attach(self, observer: AbstractParcelObserver):
        self._observers.append(observer)

    def detach(self, observer: AbstractParcelObserver):
        self._observers.remove(observer)

    def add_marker(self, marker: marker_model):
        self.__markers.append(marker)
        self.notify()

    def get_markers(self):
        return self.__markers

    def insert_marker(self, i: int, markers: List[marker_model]):
        self.__markers = markers
        self.notify()

    def notify(self):
        if len(self._observers) > 0:
            for observer in self._observers:
                observer.update(self)

    def create_signal(self):
        k = randint(1, 3)/10
        self.__signal = {i*k: round(sin(i*k), 2) for i in range(501)}
        self.notify()

    #endregion
