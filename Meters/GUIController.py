from Meters.MeterInit import MeterInit
from Meters.AbstractDevices import AbstractObserver, AbstractDevices
from UI import QConnectsWidget

class GUIController(AbstractObserver):
    def __init__(self, table: QConnectsWidget):
        self.__table = table
        self.meter = MeterInit()
        self.devices = self.meter.devices
        self.meter.attach(self)
        self.__table.clicked.connect(self.edit_data)
        self.__table.currentItemChanged.connect(self.edit_data)

    def table_show(self, showDisconnectedDevice: bool = True):
        self.__showDisconnectedDevice = showDisconnectedDevice
        self.__table.setRowCount(len(self.devices))
        for i in range(0, len(self.devices)):
            if showDisconnectedDevice or self.devices[i].isConnect:
                self.__table.addCell(i, 0, self.devices[i].name)
                self.__table.addCell(i, 1, self.devices[i].model)
                self.__table.addCell(i, 2, self.devices[i].ip)
                self.__table.addCell(i, 3, self.devices[i].port)
                self.__table.addCheckCell(i, 4, self.devices[i].isConnect)

    def edit_data(self):
        for i in range(0, len(self.devices)):
            try:
                self.meter.update_model(i, self.__table.item(i, 4).checkState(),
                                        self.__table.item(i, 2).text(),
                                        self.__table.item(i, 3).text())
            except BaseException:
                pass

    def update(self, subject: AbstractDevices):
        self.__table.clearContents()
        self.table_show(self.__showDisconnectedDevice)
