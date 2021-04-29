import sys
import threading

from PyQt5 import QtWidgets
from UI import Events, MainPage
from Test import SHowMessage
from PyQt5 import QtCore, QtGui, QtWidgets


class WindowInicilizer(QtWidgets.QMainWindow):
    def __init__(self,win):
        super().__init__()
        win.setupUi(self)

class WindowCreate():
    def render(page,connect):
        app = QtWidgets.QApplication(sys.argv)
        window = WindowInicilizer(page)
        connect(page)
        window.show()
        app.exec_()







