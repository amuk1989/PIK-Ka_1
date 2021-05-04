import sys
import threading

from UI import MainPage, optionPage,clock
from PyQt5 import QtCore, QtGui, QtWidgets

mainWindow = MainPage.Ui_MainWindow()

class WindowInicilizer(QtWidgets.QMainWindow):
    def __init__(self,win):
        super().__init__()
        win.setupUi(self)

def render():

    optionWindow = optionPage.Ui_optionPage()

    app = QtWidgets.QApplication(sys.argv)

    window = WindowInicilizer(mainWindow)
    options = WindowInicilizer(optionWindow)

    window.show()

    clock_thread = threading.Thread(target=clock.startClock, daemon=True)
    clock_thread.start()

    mainWindow.optionsButton.clicked.connect(options.show)
    mainWindow.optionsButton_1.clicked.connect(options.show)



    app.exec_()





