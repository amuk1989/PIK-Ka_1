from typing import List

from PyQt5.QtWidgets import QMessageBox

from Meters.Device import Device
from Meters.AbstractDevices import AbstractObserver
from models.singelton import singleton
from Meters.Drivers.AbstractDriver import AbstractDriver
from Meters.Drivers.DriversReg import DriversRegister
import pyvisa as visa


@singleton
class MeterInit:
    def __init__(self):
        self.__observers: List[AbstractObserver] = []
        self.rm = visa.ResourceManager()
        self.devices: List[Device] = []
        self.drivers_init()

    def drivers_init(self):
        drivers = DriversRegister().drivers
        for driver in drivers:
            self.add_device(driver)

    def add_device(self, driver: AbstractDriver):
        try:
            device = Device(driver)
            for observer in self.__observers:
                device.attach(observer)
            self.devices.append(device)
            device.notify()
        except BaseException:
            self.__error('Ошибка драйвера')

    def update_model(self, i: int, state: bool, ip: str, port: str):
        self.devices[i].port = port
        self.devices[i].ip = ip
        result = self.devices[i].connect(state)
        if result != 'Success':
            self.__error(result)

    def attach(self, observer: AbstractObserver):
        self.__observers.append(observer)
        for i in range(0, len(self.devices)):
            self.devices[i].attach(observer)

    def __error(self, message):
        self.message = QMessageBox()
        self.message.setWindowTitle('Ошибка')
        self.message.setText(message)
        self.message.setIcon(QMessageBox.Critical)
        self.message.show()
