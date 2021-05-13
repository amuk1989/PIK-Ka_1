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
parcel_controller = Parcel_controller()
input_signal_controller = inputSignalController()

class WindowInicilizer(QtWidgets.QMainWindow, QWidget):
    def __init__(self,win):
        super().__init__()
        win.setupUi(self)


def render():

    parcel = Parcel()

    app = QtWidgets.QApplication(sys.argv)

    window = WindowInicilizer(mainWindow)
    options = WindowInicilizer(optionWindow)

    window.show()

    clock_thread = threading.Thread(target=clock.startClock, daemon=True)
    clock_thread.start()

    optionWindow.modeBox.addItems(parcel_modes)
    optionWindow.modeBox.setCurrentIndex(parcel.parcel_mode)
    optionWindow.timeEdit.setText(str(parcel.detonation_time))

    mainWindow.modeBox.addItems(parcel_modes)
    mainWindow.modeBox.setCurrentIndex(parcel.parcel_mode)
    mainWindow.timeEdit.setText(str(parcel.detonation_time))

    mainWindow.optionsButton.clicked.connect(options.show)
    mainWindow.optionsButton_1.clicked.connect(options.show)
    mainWindow.okButton.clicked.connect(okButton)
    mainWindow.startButton.clicked.connect(startButton)

    optionWindow.OkButton.clicked.connect(optionOkButton)
    optionWindow.OkButton.clicked.connect(options.close)
    okButton()
    startButton()
    app.exec_()

def optionOkButton():
    parcel_controller.edit_parcel(optionWindow.modeBox.currentIndex(),optionWindow.timeEdit.text())

def okButton():
    parcel_controller.edit_parcel(mainWindow.modeBox.currentIndex(), mainWindow.timeEdit.text())

def startButton():
    input_signal_controller.set_signal()