from models.Parcel_model import Parcel
from random import triangular

class Input_simulator():
    def __init__(self):
        parcel = Parcel()
        self.count = parcel.signal_count
        self.max_power, self.min_power, self.step = parcel.get_power()
    def create_signal(self, probability: float):
        power = self.min_power
        value = {}
        while (power <= round(self.max_power, 2)):
            mode = probability
            value[power] = round(triangular(probability-0.1, probability+0.1, mode), 2)
            mode += 0.01
            power += self.step
        return value