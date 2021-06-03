from models.AbstractParcel import AbstractParcel, AbstractParcelObserver
from typing import List
from models.MarkerModel import marker_model
from simulator.InputSimulator import Input_simulator

class Chance_Programming(AbstractParcel):
    #region variables
    _graph = {}
    _observers: List[AbstractParcelObserver] = []
    _markers: List[marker_model] = []
    _name: str
    #endregion

    #region properties
    def get_mask(self):
        return 'Маркер №, N, P(N)'
    def get_label(self):
        return 'Мощность, Вт', 'Вероятность, P'
    #endregion

    #region methods
    def __init__(self):
        self.simulator = Input_simulator()
        self._name = 'COP'

    def create_signal(self):
        self.set_graph(self.simulator.create_signal(0.9))
        self.notify()
    #endregion