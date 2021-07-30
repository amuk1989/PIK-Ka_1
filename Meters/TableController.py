from Meters.MeterInit import MeterInit
from Meters.AbstractDevices import AbstractObserver, AbstractDevices
from UI import QConnectsWidget


class TableController(AbstractObserver):
    def __init__(self, table: QConnectsWidget):
        self.__table = table
        self.meter = MeterInit()
        self.devices: dict = self.meter.devices
        self.meter.attach(self)
        self.__table.clicked.connect(self.edit_data)
        self.__table.currentItemChanged.connect(self.edit_data)

    def table_show(self, showDisconnectedDevice: bool = True):
        self.__showDisconnectedDevice = showDisconnectedDevice
        self.__table.setRowCount(len(self.devices))
        for key, device in self.devices.items():
            if showDisconnectedDevice or device.isConnect:
                self.__table.addCell(key.value, 0, str(device))
                self.__table.addCell(key.value, 1, device.model)
                self.__table.addCell(key.value, 2, device.ip)
                self.__table.addCell(key.value, 3, device.port)
                self.__table.addCheckCell(key.value, 4, device.isConnect)

    def edit_data(self):
        for key in self.devices.keys():
            try:
                print(f'key {self.__table.item(key.value, 3).text()}')
                self.meter.update_model(key, self.__table.item(key.value, 4).checkState(),
                                        self.__table.item(key.value, 2).text(),
                                        self.__table.item(key.value, 3).text())
            except BaseException:
                print('TableError')

    def update_from_device(self, subject: AbstractDevices):
        self.__table.clearContents()
        self.table_show(self.__showDisconnectedDevice)
