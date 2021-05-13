from models.InputSignalModel import InputSignalModel
from models.InputSignalObserver import input_signal_observer

class inputSignalController(object):
    input_signal_observer = input_signal_observer()
    def __init__(self):
        self.input_signal = InputSignalModel()
        self.input_signal.attach(self.input_signal_observer)
    def set_signal(self):
        self.input_signal.create_signal()