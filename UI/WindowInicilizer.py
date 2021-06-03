import sys
import threading
from Controllers.ParcelController import Parcel_controller
from Controllers.InputSignalController import inputSignalController
from UI import MainPage, optionPage,clock
from PyQt5 import QtCore, QtGui, QtWidgets
from models.Parcel_model import parcel_modes, Parcel
from PyQt5.QtWidgets import *

mainWindow = MainPage.Ui_MainWindow()
optionWindow = optionPage.Ui_optionPage()

class WindowInicilizer(QtWidgets.QMainWindow, QWidget):
    def __init__(self,win):
        super().__init__()
        win.setupUi(self)

class Inicilizer():
    time_value: float
    def __init__(self):
        self.parcel_controller = Parcel_controller()
        self.input_signal_controller = inputSignalController()
        self.parcel = Parcel()
    def render(self):
        app = QtWidgets.QApplication(sys.argv)

        window = WindowInicilizer(mainWindow)
        options = WindowInicilizer(optionWindow)
        window.show()

        clock_thread = threading.Thread(target=clock.startClock, daemon=True)
        clock_thread.start()

        optionWindow.modeBox.addItems(parcel_modes)
        optionWindow.modeBox.setCurrentIndex(self.parcel.parcel_mode)
        optionWindow.timeEdit.value = self.parcel.detonation_time
        optionWindow.minPowerBox.valueChanged.connect(self.set_min_power)
        optionWindow.maxPowerBox.valueChanged.connect(self.set_max_power)
        optionWindow.stepPowerBox.valueChanged.connect(self.set_step_power)
        optionWindow.timeEdit.valueChanged.connect(self.set_time)
        optionWindow.OkButton.clicked.connect(self.optionOkButton)
        optionWindow.OkButton.clicked.connect(options.close)
        optionWindow.filePathButton.clicked.connect(self.filePathButton)

        optionWindow.typeParcelSwitch.right_position_connect(optionWindow.fileParcelBox)
        optionWindow.typeParcelSwitch.left_position_connect(optionWindow.parcelBox)

        self.time_value = self.parcel.detonation_time
        self.max_power_value, self.min_power_value, self.step_power_value = self.parcel.get_power()

        mainWindow.modeBox.addItems(parcel_modes)
        mainWindow.modeBox.setCurrentIndex(self.parcel.parcel_mode)
        mainWindow.timeEdit.value = self.parcel.detonation_time

        mainWindow.optionsButton.clicked.connect(options.show)
        mainWindow.optionsButton_1.clicked.connect(options.show)
        mainWindow.okButton.clicked.connect(self.okButton)
        mainWindow.startButton.clicked.connect(self.startButton)
        mainWindow.timeEdit.valueChanged.connect(self.set_time)

        self.okButton()
        self.startButton()
        app.exec_()

    def optionOkButton(self):
        if not optionWindow.typeParcelSwitch.state:
            self.parcel_controller.edit_parcel(optionWindow.modeBox.currentIndex(), self.time_value,
                                            optionWindow.pulseDurationBox.currentText(), self.max_power_value,
                                            self.min_power_value, self.step_power_value)
        elif optionWindow.filePathEdit.text() != '':
            file = optionWindow.filePathEdit.text()
            f = open(file, 'r')
            data = f.read()
            self.parcel_controller.edit_parcel_from_file(data)
            optionWindow.typeParcelSwitch.state = False


    def okButton(self):
        self.parcel_controller.edit_parcel(mainWindow.modeBox.currentIndex(), self.time_value,
                                           optionWindow.pulseDurationBox.currentText(), self.max_power_value,
                                           self.min_power_value, self.step_power_value)

    def startButton(self):
        self.input_signal_controller.set_signal()
        self.parcel_controller.send()

    def filePathButton(self):
        optionWindow.filePathEdit.setText(self.openFileDialog())

    def openFileDialog(self):
        return QtWidgets.QFileDialog.getOpenFileName(filter = '*txt')[0]


    def set_time(self,value: float):
        self.time_value = value
    def set_max_power(self,value: float):
        self.max_power_value = value
    def set_min_power(self,value: float):
        self.min_power_value = value
    def set_step_power(self,value: float):
        self.step_power_value = value
    def test(self):
        print('111')