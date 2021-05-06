import sys
import threading

from UI import MainPage, optionPage,clock
from PyQt5 import QtCore, QtGui, QtWidgets
from models.Parcel_model import parcel_modes
from main import parсel

mainWindow = MainPage.Ui_MainWindow()
optionWindow = optionPage.Ui_optionPage()

class WindowInicilizer(QtWidgets.QMainWindow):
    def __init__(self,win):
        super().__init__()
        win.setupUi(self)

def render():

    app = QtWidgets.QApplication(sys.argv)

    window = WindowInicilizer(mainWindow)
    options = WindowInicilizer(optionWindow)

    window.show()

    clock_thread = threading.Thread(target=clock.startClock, daemon=True)
    clock_thread.start()

    optionWindow.modeBox.addItems(parcel_modes)
    optionWindow.modeBox.setCurrentIndex(parсel.parcel_mode)
    optionWindow.timeEdit.setText(str(parсel.detonation_time))

    mainWindow.optionsButton.clicked.connect(options.show)
    mainWindow.optionsButton_1.clicked.connect(options.show)

    #mainWindow.startButton.clicked.connect()

    app.exec_()

