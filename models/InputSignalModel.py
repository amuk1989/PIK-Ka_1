from models.AbstractParcel import AbstractParcelObserver,AbstractParcel
from typing import List
from models.singelton import singleton
from math import sin

@singleton
class InputSignalModel(AbstractParcel):
    #region private variables
    __signal = {}
    _observers: List[AbstractParcelObserver] = []
    #endregion

    #region properties

    #region getters
    def set_graph(self):
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

    def notify(self):
        if len(self._observers) > 0:
            for observer in self._observers:
                observer.update(self)

    def create_signal(self):
        self.__signal = {i: sin(i) for i in range(101)}
        self.notify()

    #endregion
