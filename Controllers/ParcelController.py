from models.Parcel_model import Parcel
from models.ParcelObserver import ParcelObserver

class Parcel_controller(object):
    def __init__(self):
        self.parcel_observer = ParcelObserver()
        self.parcel = Parcel()
        self.parcel.attach(self.parcel_observer)

    def edit_parcel(self, parcel_mode_index: int, detonation_time: str):
        try:
            self.parcel.detonation_time = float(detonation_time)
            self.parcel.parcel_mode = parcel_mode_index
            self.parcel.create_signal()
        except ValueError:
            print('error')
