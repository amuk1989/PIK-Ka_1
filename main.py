import sys

from PyQt5 import QtWidgets
from Inicilizer import WindowInicilizer
from UI import MainPage

if __name__ == '__main__':
    mainWindow = MainPage.Ui_MainWindow()
    WindowInicilizer.main(mainWindow)

