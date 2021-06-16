from typing import List
from Meters.Device import Device
from Meters.AbstractDevices import AbstractObserver
from models.singelton import singleton
import pyvisa as visa

@singleton
class MeterInit():
    def __init__(self):
        self.__observers: List[AbstractObserver] = []
        self.rm = visa.ResourceManager()
        self.devices: List[Device] = []
        for i in range(0, len(self.rm.list_resources())):
            self.add_device(self.rm.list_resources()[i])

    def add_device(self, visa_addres: str):
        try:
            device = Device(self.rm.open_resource(visa_addres), visa_addres)
            for observer in self.__observers:
                device.attach(observer)
            self.devices.append(device)
            device.notify()
            return 'Success'
        except BaseException:
            return 'Не удалось подключиться'

    def get_devices_list(self):
        return self.devices

    def update_model(self, i: int, state: bool):
        self.devices[i].connect(state)

    def attach(self, observer: AbstractObserver):
        self.__observers.append(observer)
        for i in range(0, len(self.devices)):
            self.devices[i].attach(observer)
