from Meters.Drivers.AbstractDriver import AbstractDriver


class ASK4174Driver(AbstractDriver):
    def __init__(self):
        pass

    def __str__(self):
        return 'Прибор комбинированный АСК-4174'

    def get_idn(self):
        pass

    def open(self):
        pass

    def close(self):
        pass
