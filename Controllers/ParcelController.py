import Controllers.GUIController
from models.Parcel_model import Parcel
from models.ParcelObserver import ParcelObserver
from models.singelton import singleton
from typing import Any, List
import serial

@singleton
class Parcel_controller(object):
    def __init__(self):
        self.parcel_observer = ParcelObserver()
        self.parcel = Parcel()
        self.parcel.attach(self.parcel_observer)
        self.parcel.attach(Controllers.GUIController.GUIController())

    def edit_parcel(self, parcel_mode_index: int, detonation_time: float, pulse_duration: str, max_power: float,
                    min_power: float, step_power: float, parcel_count: float):
        try:
            self.parcel.detonation_time = detonation_time
            self.parcel.parcel_mode = parcel_mode_index
            self.parcel.signal_duration = int(pulse_duration)
            self.parcel.set_power(max_power, min_power, step_power)
            self.parcel.signal_count = parcel_count
            self.parcel.create_signal()
        except ValueError:
            self.parcel.create_signal()
            print('error')

    def edit_parcel_from_file(self, text_file: str):
        result = {}
        try:
            for line in text_file.split('\n'):
                key, value = line.split(' ')
                result[float(key)] = float(value)
            self.parcel.create_from_file(result)
        except ValueError:
            print('error')

    def add_marker(self, request: Any, marker) -> bool:
        if request == 'parcelWidget':
            self.parcel.add_marker(marker)
            return False
        else:
            print('lose')
            return True

    def insert_marker(self, request: Any, i: int, markers: List) -> bool:
        if request == 'parcelWidget':
            self.parcel.insert_marker(i, markers)
            return False
        else:
            print('lose')
            return True

    def delete_marker(self, request: Any, marker) -> bool:
        if request == 'parcelWidget':
            self.parcel.delete_marker(marker)
            return False
        else:
            print('lose')
            return True

    def send(self):
        parcel_in_bytes = self.parcel.bit_parcel.tobytes()
        ser = serial.serial_for_url('loop://', timeout=1)
        for i in range(0, self.parcel.signal_count):
            ser.write(parcel_in_bytes)
            data = ser.read(2)
            print(int.from_bytes(data, 'big'))
            #send_telegram(str(int.from_bytes(data, 'big')))
