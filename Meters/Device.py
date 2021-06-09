import pyvisa as visa

class Device(object):
    def __init__(self, rm: visa.ResourceManager, visa_addres: str):
        self.device = rm.open_resource(visa_addres)
        propertiesList = str(self.device.query(str("*IDN?"))).split(', ')
        self.name = propertiesList[1]
        self.ip = visa_addres.split('::')[1]

    def __get_name(self):
        return self._name
    def __set_name(self, value):
        self._name = value
    name = property(__get_name, __set_name, doc='Device name/model')

    def __get_ip(self):
        return self._ip
    def __set_ip(self, value):
        self._ip = value
    ip = property(__get_ip, __set_ip, doc='ip addres')