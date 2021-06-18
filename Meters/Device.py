from __future__ import annotations

import threading
from typing import List
from Meters.AbstractDevices import AbstractObserver
from Meters.Drivers.AbstractDriver import AbstractDriver


class Device(object):
    _observers: List[AbstractObserver] = []

    # region properties
    def __get_name(self):
        return self._name

    def __set_name(self, value):
        self._name = value

    name = property(__get_name, __set_name, doc='Driver name')

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
        self.driver = driver
        self.ip = ip
        self.port = port
        self.name = str(driver)
        self.model = ''
        self.isConnect = False

    # region methods
    def connect(self, state: bool):
        result = 'Success'
        if self.isConnect != state:
            if state:
                result = self.driver.device_init(self.ip, self.port)
                if result == 'Success':
                    self.isConnect = state
                    self.model = self.driver.get_model()
                    self.start()
                    print(f'{self.name} connected')
            else:
                self.stop()
                self.isConnect = state
                result = 'Success'
                print(f'{self.name} disconnected')
            self.notify()
        return result

    def start(self):
        self.__measure_thread = threading.Thread(target=self.driver.open, daemon=True)
        self.__measure_thread.start()

    def stop(self):
        self.__measure_thread.join()
        self.driver.close()

    def attach(self, observer: AbstractObserver):
        self._observers.append(observer)

    def detach(self, observer: AbstractObserver):
        self._observers.remove(observer)

    def notify(self):
        if len(self._observers) > 0:
            for observer in self._observers:
                observer.update(self)
    # endregion
