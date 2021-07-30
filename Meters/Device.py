from __future__ import annotations
import threading
from typing import List
from Meters.AbstractDevices import AbstractObserver
from Meters.Drivers.AbstractDriver import AbstractDriver


class Device(object):

    def __get_model(self):
        return self._model

    def __set_model(self, value):
        self._model = value

    model = property(__get_model, __set_model, doc='Device model')

    def __get_ip(self):
        return self._ip

    def __set_ip(self, value):
        self._ip = value

    ip = property(__get_ip, __set_ip, doc='ip address')

    def __get_port(self):
        return self._port

    def __set_port(self, value):
        self._port = value

    port = property(__get_port, __set_port, doc='port')

    def __get_state(self):
        return self._state

    def __set_state(self, value: bool):
        self._state = value

    isConnect = property(__get_state, __set_state, doc='connect status')

    # endregion

    def __init__(self, driver: AbstractDriver, ip: str = 'localhost', port: str = '5025'):
        self._observers: List[AbstractObserver] = []
        self.driver = driver
        self.ip = ip
        self.port = port
        self.name = driver.name
        self.model = ''
        self.isConnect = False
        self.__measure_thread = threading.Thread(target=self.driver.start, daemon=True)

    def __str__(self):
        return str(self.driver)

    # region methods
    def connect(self, state: bool):
        result = 'Success'
        if self.isConnect != state:
            if state:
                result = self.driver.connect(self.ip, self.port)
                if result == 'Success':
                    self.isConnect = state
                    self.model = self.driver.get_model()
                    print(f'{self.model} connected')
            else:
                self.stop()
                self.isConnect = state
                result = 'Success'
                print(f'{self.name} disconnected')
            self.notify()
        return result

    def start(self):
        self.driver.start_device()
        self.__measure_thread.start()

    def stop(self):
        self.driver.is_measure_active = False
        while self.__measure_thread.is_alive():
            self.__measure_thread.join()
        self.driver.close()

    def attach(self, observer: AbstractObserver):
        self._observers.append(observer)

    def detach(self, observer: AbstractObserver):
        self._observers.remove(observer)

    def notify(self):
        if len(self._observers) > 0:
            for observer in self._observers:
                observer.update_from_device(self)
    # endregion
