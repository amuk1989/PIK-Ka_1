import sys
import threading

from PyQt5 import QtWidgets
from UI import MainPage, optionPage
from Test import SHowMessage
from PyQt5 import QtCore, QtGui, QtWidgets


class WindowInicilizer(QtWidgets.QMainWindow):
    def __init__(self,win):
        super().__init__()
        win.setupUi(self)


def render():
    mainWindow = MainPage.Ui_MainWindow()
    optionWindow = optionPage.Ui_optionPage()

    app = QtWidgets.QApplication(sys.argv)

    window = WindowInicilizer(mainWindow)
    options = WindowInicilizer(optionWindow)

    window.show()

    mainWindow.optionsButton.clicked.connect(options.show)
    mainWindow.optionsButton_1.clicked.connect(options.show)

    app.exec_()





