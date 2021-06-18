from models.InputSignalModel import InputSignalModel
from models.InputSignalObserver import input_signal_observer
from models.COPObserver import COP_observer
from Controllers.AbstractHandler import AbstractHandler
from typing import Any, List
from models.singelton import singleton


@singleton
class inputSignalController(AbstractHandler):

    def __init__(self):
        self.input_signal_observer = input_signal_observer()
        self.COP_observer = COP_observer()
        self.input_signal = InputSignalModel()
        self.input_signal.attach(self.input_signal_observer)
        self.input_signal.chance_programming.attach(self.COP_observer)

    def set_signal(self):
        self.input_signal.create_signal()

    def add_marker(self, request: Any, marker) -> bool:
        if request == 'FRWidget':
            self.input_signal.add_marker(marker)
            return True
        elif request == 'COPwidget':
            self.input_signal.chance_programming.add_marker(marker)
            return True
        else:
            return super().add_marker(request, marker)

    def insert_marker(self, request: Any, i: int, markers: List) -> bool:
        if request == 'FRWidget':
            self.input_signal.insert_marker(i, markers)
            return True
        elif request == 'COPwidget':
            self.input_signal.chance_programming.insert_marker(i, markers)
            return True
        else:
            return super().insert_marker(request, i, markers)

    def delete_marker(self, request: Any, marker) -> bool:
        if request == 'FRWidget':
            self.input_signal.delete_marker(marker)
            return True
        elif request == 'COPwidget':
            self.input_signal.chance_programming.delete_marker(marker)
            return True
        else:
            return super().delete_marker(request, marker)
