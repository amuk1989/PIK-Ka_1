from models.InputSignalModel import InputSignalModel
from models.InputSignalObserver import input_signal_observer
from Controllers.AbstractHandler import AbstractHandler
from typing import Any, List
from models.singelton import singleton

@singleton
class inputSignalController(AbstractHandler):
    input_signal_observer = input_signal_observer()
    def __init__(self):
        self.input_signal = InputSignalModel()
        self.input_signal.attach(self.input_signal_observer)

    def set_signal(self):
        self.input_signal.create_signal()

    def add_marker(self, request: Any, marker) -> bool:
        if request == 'FRWidget':
            self.input_signal.add_marker(marker)
            return True
        else:
            return super().add_marker(request, marker)

    def insert_marker(self, request: Any, i: int, markers: List) -> bool:
        if request == 'FRWidget':
            self.input_signal.insert_marker(i, markers)
            return True
        else:
            return super().insert_marker(request, i, markers)