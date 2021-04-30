import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class WindowInicilizer(QtWidgets.QMainWindow):
    def __init__(self,win):
        super().__init__()
        win.setupUi(self)

class WindowCreate():
    def __init__(self):
        pass

    def render(page,connect):
        app = QtWidgets.QApplication(sys.argv)
        window = WindowInicilizer(page)
        connect
        window.show()
        app.exec_()







