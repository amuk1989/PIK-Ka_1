same_data = [
    1,
    3,
    5,
    2,
    0,
]

parcel_modes = [
    'Режим программирования',
    'Режим контактного датчика',
    'Режим самоликвидации',
]

class Parcel(object):
    def __init__(self):
        self.__parcel_mode = 0
        self.__detonation_time = 2
        self.__signal = same_data

    @property
    def signal(self):
        return self.__signal

    @property
    def parcel_mode(self):
        return self.__parcel_mode

    @property
    def detonation_time(self):
        return self.__detonation_time

    @parcel_mode.setter
    def parcel_mode(self,value):
        self.__parcel_mode = value

    @detonation_time.setter
    def detonation_time(self,value):
        self.__detonation_time = value

    def create_signal(self):
        list[
            0,

        ]
