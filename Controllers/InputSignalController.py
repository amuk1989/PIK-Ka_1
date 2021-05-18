from models.InputSignalModel import InputSignalModel
from models.InputSignalObserver import input_signal_observer
from Controllers.AbstractHandler import AbstractHandler
from typing import Any
from models.singelton import singleton

@singleton
class inputSignalController(AbstractHandler):
    input_signal_observer = input_signal_observer()
    def __init__(self):
        self.input_signal = InputSignalModel()
        self.input_signal.attach(self.input_signal_observer)

    def set_signal(self):
        self.input_signal.create_signal()

    def handle(self, request: Any, marker) -> bool:
        if request == 'FRWidget':
            self.input_signal.add_marker(marker)
            return True
        else:
            return super().handle(request, marker)