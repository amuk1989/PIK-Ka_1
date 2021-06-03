from models.AbstractParcel import AbstractParcelObserver,AbstractParcel
from typing import List
from models.singelton import singleton
from math import sin
from models.MarkerModel import marker_model
from models.ChanceOfProgramming import Chance_Programming
from random import randint

@singleton
class InputSignalModel(AbstractParcel):
    #region public variables
    chance_programming: Chance_Programming
    #endregion
    #region private variables
    _graph = {}
    _observers: List[AbstractParcelObserver] = []
    _markers: List[marker_model] = []
    _name = ''
    #endregion

    #region properties
    def get_mask(self):
        return 'Маркер №, A, Ч'

    def get_label(self):
        return 'Частота, ГГц', 'Амплитуда'
    #endregion

    #region Methods
    def __init__(self):
        self.create_signal()
        self._name = 'InputSignal'

    def create_signal(self):
        k = randint(1, 3)/10
        self.set_graph({i*k: round(sin(i*k), 2) for i in range(501)})
        self.chance_programming = Chance_Programming()
        self.chance_programming.create_signal()
        self.notify()
    #endregion
