import math
from threading import Lock
from time import sleep

import numpy as np
from Enums import DeviceName
from Meters.Drivers.AbstractDriver import AbstractDriver, visa
from models.Parcel_model import Parcel
from Controllers.GUIController import GUIController


class G7M50Driver(AbstractDriver):
    def __init__(self):
        self.frequency: float = 0
        #self.power = self.__power_calculate(40)
        self.is_measure_active = False
        self.parcel = Parcel()
        self.name = DeviceName.generator
        self.gui = GUIController()
        self.lock = Lock()

    def __str__(self):
        return 'Генератор Г7М-50'

    def connect(self, ip: str, port: str):
        ip = '172.16.17.106'
        port = '5025'
        visa_address = f'TCPIP::{ip}::{port}::SOCKET'
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

    def get_idn(self):
        idn = self.device.query('*IDN?')
        return idn

    def start(self):
        self.frequency = self.parcel.frequency
        count = self.parcel.signal_count
        self.power = self.power[0]
        distance = 40
        self.start_device()
        self.device_config()
        while self.is_measure_active:
            if self.power >= self.parcel.power[1]:
                duration_on, duration_off, duration_repeat = self.__get_impuls_burst()
                count_signals = math.ceil(len(duration_on)/200)
                self.write(f'SOUR:POW:LEV {self.power}DBM')
                self.power -= self.parcel.power[2]#self.__power_calculate(distance)
                self.giu_update()
                duration_on_list = np.array_split(duration_on, count_signals)
                duration_off_list = np.array_split(duration_off, count_signals)
                duration_repeat_list = np.array_split(duration_repeat, count_signals)
                for i in range(0, len(duration_on_list)):
                    self.write(f'PULM:INT:TRA:ONT {",".join(duration_on_list[i])}')
                    while not self.wait_answer():
                        sleep(0.5)
                        print(f'wait')
                    self.write(f'PULM:INT:TRA:REP {",".join(duration_repeat_list[i])}')
                    while not self.wait_answer():
                        sleep(0.5)
                        print(f'wait')
                    self.write(f'PULM:INT:TRA:OFFT {",".join(duration_off_list[i])}')
                    print(f'PULM:INT:TRA:OFFT {",".join(duration_off_list[i])}')
                    while not self.wait_answer():
                        sleep(0.5)
                        print(f'wait')
                    self.write('INIT:IMM')
                    while not self.wait_answer():
                        sleep(0.5)
                        print(f'wait')
                    if not self.is_measure_active:
                        break
                distance += 5
            else:
                self.is_measure_active = False
                break
        self.write('SYSTem:SECurity:DISPlay:RESTricted ON')
        self.write('SYSTem:SECurity:DISPlay OFF')
        self.gui.stop_measuer()
        self.stop()

    def start_device(self):
        self.write('SOURce:FREQuency:MODE CW')
        self.write(f'SOUR:FREQ {self.frequency} GHz')
        self.write(f'SOUR:POW:LEV {self.power} DBM')
        self.write('SOUR:PULM:SOUR:INT PTRA')
        self.write('SOUR:PULM:STAT ON')
        self.giu_update()

    def stop(self):
        self.is_measure_active = False
        self.write('ABOR')
        self.write('OUTPut:STAT OFF')

    def close(self):
        self.stop()
        self.device.clear()
        self.device.close()
        return 'Success'

    def device_config(self):
        self.is_measure_active = True
        self.write('SYSTem:SECurity:DISPlay:RESTricted OFF')
        self.write('SYSTem:SECurity:DISPlay ON')
        self.write('ABORt')
        self.write('FREQuency:MODE SWEep')
        self.write('SOURce:LIST:TRIGger:SOURce IMM')
        self.write('FREQuency:STARt 1GHz')
        self.write('FREQuency:STOP 1GHz')
        self.write('SWEep:POINts 2')
        self.write('POWer:MODE FIXed')
        self.write('POWer:ALC:STATe OFF')
        self.write('POWer:LEVel:IMMediate:AMPLitude 10DBM')
        self.write('OUTPut:STATe ON')
        self.write('TRIGger:OUTPut:MODE SWEEPSTART')
        self.write('TRIGger:OUTPut:DURation 100us')
        self.write('TRIG:SEQ:SOURce IMMediate')
        self.write('PULM:STATe ON')
        self.write('PULM:INTernal:TRAin:TRIGger TRIGgered')
        self.write('PULM:SOURce INTernal')
        self.write('PULM:SOURce:INTernal PTRAin')
        self.write('INITiate:CONTinuous OFF')

    def giu_update(self):
        self.gui.update_from_generator(self.power, self.frequency)

    def write(self, command: str):
        self.lock.acquire()
        self.device.write(command, termination='\n')
        self.device.write("*OPC")
        self.lock.release()

    def query(self, command: str) -> str:
        try:
            self.lock.acquire()
            result = self.device.query(command)
            while not self.wait_answer():
                print('1')
            return result
        finally:
            self.lock.release()

    def wait_answer(self) -> bool:
        try:
            self.lock.acquire()
            result = self.device.query("*OPC?")
            if result == '+1':
                return True
            else:
                return False
        except BaseException:
            return False
        finally:
            self.lock.release()

    def __power_calculate(self, distance: float):
        result = (37.0 - 20 * (math.log10(distance / 5.0)))
        return round(result, 3)

    def __get_impuls_burst(self):
        count = self.parcel.signal_count
        duration = (1 / self.parcel.signal_duration) * (10 ** 3)
        bit = 0
        bit_count = 0
        result = []
        result_on = []
        result_off = []
        result_repeat = []
        for i in self.parcel.uart_bits.values():
            if i != bit:
                result.append(bit_count * duration)
                bit_count = 1
                bit = i
            else:
                bit_count += 1
        result.append(bit_count * duration)
        for j in range(0, count):
            for i in range(0, len(result)):
                if i % 2 == 0:
                    result_on.append(f'{round(result[i], 3)}ms')
                else:
                    result_off.append(f'{round(result[i], 3)}ms')
                    result_repeat.append('1')

        return result_on, result_off, result_repeat
