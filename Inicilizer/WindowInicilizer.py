import sys
import threading

from PyQt5 import QtWidgets
from UI import Events


class WindowInicilizer(QtWidgets.QMainWindow):
    def __init__(self,win):
        super().__init__()
        win.setupUi(self)
        #x = threading.Thread(target=Events.Events, args=(1,), daemon=True)
        #x.start()




def main(page):
    app = QtWidgets.QApplication(sys.argv)
    window = WindowInicilizer(page)

    window.show()
    app.exec_()

