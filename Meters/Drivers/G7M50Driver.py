from time import sleep
from Enums import DeviceName
from Meters.Drivers.AbstractDriver import AbstractDriver, visa
from models.Parcel_model import Parcel


class G7M50Driver(AbstractDriver):
    def __init__(self):
        self.power = 13.0
        self.is_measure_active = False
        self.parcel = Parcel()
        self.name = DeviceName.generator

    def __str__(self):
        return 'Генератор Г7М-50'

    def device_init(self, ip: str, port: str):
        ip = '172.16.17.106'
        port = '5025'
        visa_address = f'TCPIP0::{ip}::{port}::SOCKET'
        rm = visa.ResourceManager()
        try:
            self.device = rm.open_resource(visa_address, read_termination='\n')
            idn = self.get_idn()
            self._model = str(idn).split(',')[1]
            self.write('*RST')
            self.write('*CLS')
            self.start_device()
            return 'Success'
        except BaseException:
            return 'Ошибка подключения'

    def min_range_set(self, value: float):
        pass

    def max_range_set(self, value: float):
        pass

    def get_idn(self):
        idn = self.device.query('*IDN?')
        return idn

    def start(self):
        self.write('OUTPut:STAT ON')
        self.is_measure_active = True
        while self.is_measure_active:
            if self.power > -30:
                self.power = self.power - 1.0
                self.write(f'SOUR:POW:LEV {self.power}DBM')
                sleep(1)
            else:
                self.stop()
                break

    def get_measure_data(self):
        pass

    def start_device(self):
        self.write('SOUR:FREQ:MODE CW')
        self.write('SOUR:POWer:MODE FIXed')
        self.write('SOUR:FREQ 34.00GHz')
        self.write(f'SOUR:POW:LEV {self.power}DBM')

    def stop(self):
        self.write('OUTPut:STAT OFF')

    def close(self):
        self.write('OUTPut:STAT OFF')
        self.device.clear()
        self.device.close()
        return 'Success'

    def set_range(self, start: float, value: float, dots_count: int):
        pass

    def get_range(self):
        pass

    def set_min_range(self, value: float):
        pass

    def set_max_range(self, value: float):
        pass

    def write(self, command: str):
        self.device.write(command, termination='\n')
        while not self.wait_answer():
            print('1')

    def query(self, command: str) -> str:
        try:
            #self.__lock.acquire()
            result = self.device.query(command)
            while not self.wait_answer():
                print('1')
            return result
        finally:
            pass#self.__lock.release()

    def wait_answer(self) -> bool:
        result = self.device.query("*OPC?")
        if result == '+1':
            return True
        else:
            return False