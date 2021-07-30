import math
from threading import Lock
from time import sleep
from Enums import DeviceName
from Meters.Drivers.AbstractDriver import AbstractDriver, visa
from models.Parcel_model import Parcel
from Controllers.GUIController import GUIController


class G7M50Driver(AbstractDriver):
    def __init__(self):
        self.power = self.__power_calculate(40)
        self.frequency = 34
        self.is_measure_active = False
        self.parcel = Parcel()
        self.name = DeviceName.generator
        self.gui = GUIController()
        self.__lock = Lock()

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
            print(self.__get_impuls_burst())
            return 'Success'
        except BaseException:
            return 'Ошибка подключения'

    def get_idn(self):
        idn = self.device.query('*IDN?')
        return idn

    def start(self):
        print(self.__get_impuls_burst())
        duration_on, duration_off, duration_repeat = self.__get_impuls_burst()
        self.write('PULM:INT:TRA:LIST:PRES')
        self.write(f'PULM:INT:TRA:REP {duration_repeat}')
        self.write(f'PULM:INT:TRA:ONT {duration_on}')
        self.write(f'PULM:INT:TRA:OFFT {duration_off}')
        self.write('OUTPut:STAT ON')
        #self.write('PULM:INT:TRA:TRIG:IMM')
        self.is_measure_active = True
        distance = 40
        while self.is_measure_active:
            if distance <= 200:
                self.power = self.__power_calculate(distance)
                self.write(f'SOUR:POW:LEV {self.power}DBM')
                self.giu_update()
                distance += 5
                sleep(1)
            else:
                self.stop()
                self.is_measure_active = False
                break

    def start_device(self):
        self.write('SOUR:FREQ:MODE CW')
        self.write('SOUR:POWer:MODE FIXed')
        self.write(f'SOUR:FREQ {self.frequency}GHz')
        self.write(f'SOUR:POW:LEV {self.power}DBM')
        self.write('PULM:STAT ON')
        self.write('PULM:SOUR:INT PTRA')
        self.giu_update()

    def stop(self):
        self.write('OUTPut:STAT OFF')

    def close(self):
        self.stop()
        self.device.clear()
        self.device.close()
        return 'Success'

    def giu_update(self):
        self.gui.update_from_generator(self.power, self.frequency)

    def write(self, command: str):
        self.__lock.acquire()
        self.device.write(command, termination='\n')
        #while not self.wait_answer():
        #    print('1')
        self.__lock.release()

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

    def __power_calculate(self, distance: float):
        result = 37.0 - 20 * (math.log10(distance / 5.0))
        return round(result, 3)

    def __get_impuls_burst(self):
        duration = (1 / self.parcel.signal_duration) * (10 ** 3)
        bit = 0
        bit_count = 0
        result = []
        result_on = ''
        result_off = ''
        result_repeat = ''
        for i in self.parcel.uart_bits.values():
            if i != bit:
                result.append(bit_count * duration)
                bit_count = 1
                bit = i
            else:
                bit_count += 1
        result.append(bit_count * duration)
        print(result)
        for i in range(0, len(result)):
            if i % 2 == 0:
                result_on += f'{round(result[i], 4)}ms,'
            else:
                result_off += f'{round(result[i], 4)}ms,'
                result_repeat += '1,'
        return result_on, result_off, result_repeat
