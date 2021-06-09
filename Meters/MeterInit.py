from typing import List
from Meters.Device import Device
from UI.QConnectsWidget import QConnectsWidget
import pyvisa as visa

class MeterInit():
    def __init__(self):
        rm = visa.ResourceManager()
        self.devices: List[Device] = []
        for i in range(0, len(rm.list_resources())):
            device = Device(rm, rm.list_resources()[i])
            self.devices.append(device)

    def get_devices_list(self, filter: str = ''):
        return self.devices

    def table_show(self, table: QConnectsWidget, fields: List[int] = [0,]):
        table.setRowCount(len(self.devices))
        for i in range(0, len(self.devices)):
            table.addCell(i, 0, self.devices[i].name)
            table.addCell(i, 1, self.devices[i].ip)
            table.addCheckCell(i, 2)
