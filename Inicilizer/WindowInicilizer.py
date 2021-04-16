import sys

from PyQt5 import QtWidgets


class WindowInicilizer(QtWidgets.QMainWindow):
    def __init__(self,win):
        super().__init__()
        win.setupUi(self)

def main(page):
    app = QtWidgets.QApplication(sys.argv)
    window = WindowInicilizer(page)
    window.show()
    app.exec_()

