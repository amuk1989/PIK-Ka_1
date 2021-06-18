from Meters.Drivers.AbstractDriver import AbstractDriver
import pyvisa as visa


class SK4MDriver(AbstractDriver):
    def __init__(self):
        self._model: str = ''

    def __str__(self):
        return 'Анализатор спектра СК4М'

    def device_init(self, ip: str, port: str):
        visa_address = f'TCPIP::{ip}::{port}::SOCKET'
        rm = visa.ResourceManager()
        try:
            self.device = rm.open_resource(visa_address, read_termination='\n')
            idn = self.get_idn()
            self._model = str(idn).split(', ')[1]
            return 'Success'
        except BaseException:
            return 'Ошибка подключения'

    def get_idn(self):
        idn = self.device.query('*IDN?');
        return idn

    def open(self):
        while True:
            self.device.write('INIT', termination='\n')

    def close(self):
        self.device.write('ABORt', termination='\n')
        self.device.clear()
        self.device.close()
        return 'Success'
