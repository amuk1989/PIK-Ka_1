import time
from threading import Lock

from Controllers.InputSignalController import inputSignalController
from Meters.Drivers.AbstractDriver import AbstractDriver
from Enums import DeviceName
import pyvisa as visa


class SK4MDriver(AbstractDriver):
    # region properties
    def min_range_set(self, value: float):
        self.write(f'SENS:FREQ:STAR {value} GHZ')
        self.get_range()

    def max_range_set(self, value: float):
        self.write(f'SENS:FREQ:STOP {value} GHZ')
        self.get_range()

    def span_set(self, value: float):
        self.device.write(f'SENS:FREQ:SPAN {value} GHZ', termination='\n')
        self.get_range()

    def dots_count_range_set(self, value: int):
        self.device.write(f'SENS:SWE:POIN {value}', termination='\n')
        self.get_range()

    # endregion

    def __init__(self):
        self.device: visa.Resource
        self._model: str = ''
        self.name = DeviceName.spectrum_analizer
        self.input_signal_controller = inputSignalController()
        self._measure_data = []
        self.__lock = Lock()

    def __str__(self):
        return 'Анализатор спектра СК4М'

    # region methods
    def device_init(self, ip: str, port: str):
        visa_address = f'TCPIP::{ip}::{port}::SOCKET'
        rm = visa.ResourceManager()
        try:
            self.device = rm.open_resource(visa_address, read_termination='\n')
            self.write('DISPlay:VISible OFF')
            idn = self.get_idn()
            self._model = str(idn).split(', ')[1]
            self.write('CALCulate:PARameter:DELete:ALL')
            self.write('*CLS')
            self.write('FORM ASCii')
            self.get_range()
            return 'Success'
        except BaseException:
            return 'Ошибка подключения'

    def get_idn(self):
        idn = self.query('*IDN?')
        return idn

    def get_range(self):
        self.min_range = float(self.query('SENS:FREQ:STAR?')) / 1e9#self.device.query(f'SENS:FREQ:STAR?')) / 1e9
        self.max_range = float(self.query('SENS:FREQ:STOP?')) / 1e9
        try:
            self.span_range = float(self.device.query(f'SENS:F REQ:SPAN?')) / 1e9
        except ValueError:
            self.span_range = self.max_range - self.min_range
        self.dots_count_range = int(self.query('SENS:SWE:POIN?'))
        self.x_data = []
        for i in range(self.dots_count_range):
            self.x_data.append(self.min_range + i * (self.span_range / self.dots_count_range))

    def start_device(self):
        self.write('CALC:PAR:DEF "PIK_Ka_trace", POWer')#self.device.write('CALC:PAR:DEF "PIK_Ka_trace", POWer', termination='\n')
        self.write('CALC:PAR:SEL "PIK_Ka_trace"')
        self.write('INIT:CONT ON')
        self.write('INIT')

    def get_measure_data(self):
        string_data: str = ''
        while True:
            string_data: str = self.query('CALC:DATA? FDATA')#self.device.query('CALC:DATA? FDATA')
            if string_data != '':
                break
        string_list_data = string_data.split(',')
        data = [float(string_list_data[i]) for i in range(0, len(string_list_data))]
        for number in data:
            if number not in self.measure_data:
                self.measure_data = data
                return True
        return False

    def start(self):
        self.is_measure_active = True
        while self.is_measure_active:
            if self.get_measure_data() and len(self.x_data) == len(self.measure_data):
                self.input_signal_controller.set_signal(self.x_data, self.measure_data)

    def stop(self):
        lock = Lock()
        lock.acquire()
        try:
            self.is_measure_active = False
        finally:
            lock.release()
        self.write('ABORt')

    def close(self):
        self.stop()
        self.device.clear()
        self.device.close()
        return 'Success'

    def write(self, command: str):
        self.device.write(command, termination='\n')
        while not self.wait_answer():
            print('1')

    def query(self, command: str) -> str:
        try:
            self.__lock.acquire()
            result = self.device.query(command)
            while not self.wait_answer():
                print('1')
            return result
        finally:
            self.__lock.release()

    def wait_answer(self) -> bool:
        result = self.device.query("*OPC?")
        if result == '+1':
            return True
        else:
            return False

    # endregion
