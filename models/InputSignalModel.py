from models.AbstractParcel import AbstractParcelObserver,AbstractParcel
from typing import List
from models.singelton import singleton
from math import sin
from models.MarkerModel import marker_model

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
    #endregion

    #region setters

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
        print(f'add marker {marker}')
        self.__markers.append(marker)
        self.notify()

    def get_markers(self):
        return self.__markers

    def notify(self):
        if len(self._observers) > 0:
            for observer in self._observers:
                observer.update(self)

    def create_signal(self):
        self.__signal = {i*0.1: sin(i*0.1) for i in range(501)}
        self.notify()

    #endregion
