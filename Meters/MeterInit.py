from typing import List
from PyQt5.QtWidgets import QMessageBox
from Meters.Device import Device
from Meters.AbstractDevices import AbstractObserver
from Meters.Drivers.G7M50Driver import G7M50Driver
from Meters.Drivers.SK4MDriver import SK4MDriver
from models.singelton import singleton
from Meters.Drivers.AbstractDriver import AbstractDriver
from Meters.Drivers.DriversReg import DriversRegister
from Controllers.GUIController import GUIController
from Enums import DeviceName
import pyvisa as visa


@singleton
class MeterInit:

    def __init__(self):
        self.__observers: List[AbstractObserver] = []
        self.rm = visa.ResourceManager()
        self.devices: dict = {}
        self.drivers_init()
        gui_controller = GUIController()
        self.attach(gui_controller)

    def drivers_init(self):
        #drivers = DriversRegister().drivers
        #for driver in drivers:
        #    self.add_device(driver)
        self.devices[DeviceName.spectrum_analizer] = Device(SK4MDriver())
        self.devices[DeviceName.generator] = Device(G7M50Driver())
        #print(self.devices)

    def add_device(self, driver: AbstractDriver):
        try:
            device = Device(driver)
            self.devices[device.name] = device
            device.notify()
        except BaseException:
            self.__error('Ошибка драйвера')

    def update_model(self, key: DeviceName, state: bool, ip: str, port: str):
        self.devices[key].port = port
        self.devices[key].ip = ip
        result = self.devices[key].connect(state)
        if result != 'Success':
            self.__error(result)

    def attach(self, observer: AbstractObserver):
        self.__observers.append(observer)
        for item in self.devices.values():
            item.attach(observer)

    def start_measure(self):
        for device in self.devices.values():
            device.start()

    def stop_measure(self):
        for device in self.devices.values():
            device.stop()

    def __error(self, message):
        self.message = QMessageBox()
        self.message.setWindowTitle('Ошибка')
        self.message.setText(message)
        self.message.setIcon(QMessageBox.Critical)
        self.message.show()
