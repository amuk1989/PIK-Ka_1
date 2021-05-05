from models.Enums import ParcelMode

class parcel(object):
    __parcel_mode = ParcelMode.programming
    __detonation_time = 5

    parcel_mode = property()
    detonation_time = property()

    @parcel_mode.getter
    def parcel_mode(self):
        return self.__parcel_mode

    @detonation_time.getter
    def detonation_time(self):
        return self.__detonation_time

    @parcel_mode.setter
    def parcel_mode(self,value):
        self.__parcel_mode = value

    @detonation_time.setter
    def detonation_time(self,value):
        self.__detonation_time = value
