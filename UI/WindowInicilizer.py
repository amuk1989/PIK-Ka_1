import sys
import threading
from Controllers.ParcelController import Parcel_controller
from Enums import DeviceName
from UI import MainPage, optionPage, ConnectPage, clock
from PyQt5 import QtWidgets
from models.Parcel_model import parcel_modes, Parcel
from PyQt5.QtWidgets import *
from Meters.TableController import TableController
from Meters.MeterInit import MeterInit

mainWindow = MainPage.Ui_MainWindow()
optionWindow = optionPage.Ui_optionPage()
connectsWindow = ConnectPage.Ui_connectionPage()


class WindowInicilizer(QtWidgets.QMainWindow, QWidget):
    def __init__(self, win):
        super().__init__()
        win.setupUi(self)


class Inicilizer():
    time_value: float

    def __init__(self):
        self.parcel_controller = Parcel_controller()
        self.parcel = Parcel()
        self.meter = MeterInit()

    def render(self):
        app = QtWidgets.QApplication(sys.argv)

        self.window = WindowInicilizer(mainWindow)
        self.options = WindowInicilizer(optionWindow)
        self.connects = WindowInicilizer(connectsWindow)

        self.connectGuiController = TableController(connectsWindow.connectionTable)
        self.mainWinConnectGuiController = TableController(mainWindow.tableWidget)
        self.mainWinConnectGuiController.table_show(showDisconnectedDevice=False)
        self.window.show()

        clock_thread = threading.Thread(target=clock.startClock, daemon=True)
        clock_thread.start()

        # region option
        optionWindow.modeBox.addItems(parcel_modes)
        optionWindow.modeBox.setCurrentIndex(self.parcel.parcel_mode)
        optionWindow.timeEdit.value = self.parcel.detonation_time
        optionWindow.minPowerBox.valueChanged.connect(self.set_min_power)
        optionWindow.maxPowerBox.valueChanged.connect(self.set_max_power)
        optionWindow.stepPowerBox.valueChanged.connect(self.set_step_power)
        optionWindow.timeEdit.valueChanged.connect(self.set_time)
        optionWindow.parcelCountBox.valueChanged.connect(self.set_parcel_count)
        optionWindow.parcelCountBox.setValue(self.parcel.signal_count)
        optionWindow.OkButton.clicked.connect(self.optionOkButton)
        optionWindow.filePathButton.clicked.connect(self.filePathButton)

        optionWindow.typeParcelSwitch.right_position_connect(optionWindow.fileParcelBox)
        optionWindow.typeParcelSwitch.left_position_connect(optionWindow.parcelBox)

        optionWindow.powerSwitch.right_position_connect(optionWindow.powerBox)
        optionWindow.powerSwitch.left_position_connect(optionWindow.rangePowerBox)
        #optionWindow.destroyed.connect(self.meter.stop_measure)
        # endregion

        # region connectWindow
        connectsWindow.addDeviceButton.clicked.connect(self.add_device_button)
        # endregion

        self.time_value = self.parcel.detonation_time
        self.max_power_value, self.min_power_value, self.step_power_value = self.parcel.get_power()
        self.parcel_count_value = self.parcel.signal_count

        # region Main
        mainWindow.optionsButton.clicked.connect(self.options.show)
        mainWindow.optionsButton_1.clicked.connect(self.options.show)
        mainWindow.startButton.clicked.connect(self.startButton)
        mainWindow.startButton_2.clicked.connect(self.startButton)

        mainWindow.modeBox.addItems(parcel_modes)
        mainWindow.timeEdit.valueChanged.connect(self.timeEdit)

        mainWindow.powerSwitch.left_position_connect(mainWindow.rangePowerBox)
        mainWindow.powerSwitch.right_position_connect(mainWindow.powerBox)

        mainWindow.connectOptionsButton.clicked.connect(self.connect_option_win)
        mainWindow.frequencyMinBox.valueChanged.connect(self.set_min_frequency)
        mainWindow.frequencyMaxBox.valueChanged.connect(self.set_max_frequency)
        mainWindow.dotsCountBox.valueChanged.connect(
                                            self.meter.devices[DeviceName.spectrum_analizer].driver.dots_count_range_set
                                            )
        mainWindow.parcelCountLabel.setText(mainWindow.parcelCountBox.text())
        mainWindow.parcelCountBox.valueChanged.connect(self.parcel_count_edit)
        self.window.destroyed.connect(self.meter.stop_measure)
        # endregion

        self.okButton()
        app.exec_()

    def set_min_frequency(self, value: float):
        if value < mainWindow.frequencyMaxBox.value():
            self.meter.devices[DeviceName.spectrum_analizer].driver.min_range_set(value)

    def set_max_frequency(self, value: float):
        if value > mainWindow.frequencyMinBox.value() + 0.1 ** mainWindow.frequencyMinBox.decimals():
            self.meter.devices[DeviceName.spectrum_analizer].driver.max_range_set(value)

    def optionOkButton(self):
        if not optionWindow.typeParcelSwitch.state:
            self.parcel_controller.edit_parcel(optionWindow.modeBox.currentIndex(), self.time_value,
                                               optionWindow.pulseDurationBox.currentText(), self.max_power_value,
                                               self.min_power_value, self.step_power_value, self.parcel_count_value)
            self.options.close()
        elif optionWindow.filePathEdit.text() != '':
            file = optionWindow.filePathEdit.text()
            f = open(file, 'r')
            data = f.read()
            self.parcel_controller.edit_parcel_from_file(data)
            optionWindow.typeParcelSwitch.state = False
            self.options.close()
        else:
            print('error')

    def okButton(self):
        self.parcel_controller.edit_parcel(mainWindow.modeBox.currentIndex(), self.time_value,
                                           optionWindow.pulseDurationBox.currentText(), self.max_power_value,
                                           self.min_power_value, self.step_power_value, self.parcel_count_value)

    def startButton(self):
        self.meter.start_measure()
        #self.parcel_controller.send()

    def timeEdit(self, value):
        self.set_time(value)
        self.okButton()

    def parcel_count_edit(self, value: int):
        #self.parcel_count_value(value)
        self.okButton()

    def filePathButton(self):
        optionWindow.filePathEdit.setText(self.openFileDialog())

    def openFileDialog(self):
        return QtWidgets.QFileDialog.getOpenFileName(filter='*txt')[0]

    def okStart(self):
        self.okButton()
        self.startButton()

    def optionOkStart(self):
        self.optionOkButton()
        self.startButton()

    def connect_option_win(self):
        self.connects.show()
        self.connectGuiController.table_show()

    def add_device_button(self):
        pass

    def set_time(self, value: float):
        self.time_value = value

    def set_max_power(self, value: float):
        self.max_power_value = value

    def set_min_power(self, value: float):
        self.min_power_value = value

    def set_step_power(self, value: float):
        self.step_power_value = value

    def set_parcel_count(self, value: int):
        self.parcel_count_value = value

    def test(self):
        print('111')
