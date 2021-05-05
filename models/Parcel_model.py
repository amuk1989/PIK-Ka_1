from Enums import ParcelMode

class parcel(object):
    __parcel_mode = ParcelMode.self_destruct
    __detonation_time = 2

    #parcel_mode = property()
    #detonation_time = property()

    @property
    def parcel_mode(self):
        return self.__parcel_mode

    @property
    def detonation_time(self):
        #print(str(self.__detonation_time))
        return self.__detonation_time

    @parcel_mode.setter
    def parcel_mode(self,value):
        self.__parcel_mode = value

    @detonation_time.setter
    def detonation_time(self,value):
        self.__detonation_time = value
