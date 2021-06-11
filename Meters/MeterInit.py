from typing import List
from Meters.Device import Device
from UI.QConnectsWidget import QConnectsWidget
from Meters.AbstractDevices import AbstractDevices,AbstractObserver
from models.singelton import singleton
import pyvisa as visa

@singleton
class MeterInit():
    def __init__(self):
        self.rm = visa.ResourceManager()
        self.devices: List[Device] = []
        for i in range(0, len(self.rm.list_resources())):
            self.add_device(self.rm.list_resources()[i])

    def add_device(self, visa_addres: str):
        device = Device(self.rm, visa_addres)
        self.devices.append(device)

    def get_devices_list(self, filter: str = ''):
        return self.devices

    def update_model(self, i: int, state: bool):
        self.devices[i].connect(state)

    def attach(self, observer: AbstractObserver):
        for i in range(0, len(self.devices)):
            self.devices[i].attach(observer)
