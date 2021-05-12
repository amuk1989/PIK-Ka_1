from models.Parcel_model import Parcel
from models.ParcelObserver import ParcelObserver

class Parcel_controller(object):
    parcel_observer = ParcelObserver()

    def __init__(self):
        self.parcel = Parcel()
        print(self.parcel)
        self.parcel.attach(self.parcel_observer)

    def edit_parcel(self, parcel_mode_index, detonation_time):
        self.parcel.detonation_time = detonation_time
        self.parcel.parcel_mode = parcel_mode_index