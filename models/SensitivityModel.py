from models.AbstractParcel import AbstractParcelObserver, AbstractParcel
from typing import List
from models.MarkerModel import marker_model

class Sensitivity_model(AbstractParcel):
    # region variables
    _graph = {}
    _observers: List[AbstractParcelObserver] = []
    _markers: List[marker_model] = []
    _name = ''
    # endregion

    # region properties
    def get_mask(self):
        return 'Маркер №, P(N), N Вт'

    def get_label(self):
        return '', ''
    # endregion
    def __init__(self):
        self._name = 'Sensitivity'
