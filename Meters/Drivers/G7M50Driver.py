from Meters.Drivers.AbstractDriver import AbstractDriver, visa
from models.Parcel_model import Parcel


class G7M50Driver(AbstractDriver):
    def __init__(self):
        self.parcel = Parcel()

    def __str__(self):
        return 'Генератор Г7М-50'

    def device_init(self, ip: str, port: str):
        visa_address = f'TCPIP::{ip}::{port}::INSTR'
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
        pass
        #self.device.query('')

    def close(self):
        self.device.clear()
        self.device.close()
        return 'Success'
