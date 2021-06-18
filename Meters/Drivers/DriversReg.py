#Список драйверов
from Meters.Drivers.SK4MDriver import SK4MDriver
from Meters.Drivers.ASK3172Driver import ASK3172Driver
from Meters.Drivers.G7M50Driver import G7M50Driver
from Meters.Drivers.ASK4174Driver import ASK4174Driver


class DriversRegister:
    def __init__(self):
        self.drivers = [
            SK4MDriver(),
            ASK3172Driver(),
            G7M50Driver(),
            ASK4174Driver(),
        ]
