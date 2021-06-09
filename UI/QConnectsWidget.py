import threading

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QWidget

class QConnectsWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.resizeColumnsToContents()
    def addRow(self):
        self.setRowCount(self.rowCount()+1)
    def addCell(self, row: int, column: int, value: str = ''):
        item = QtWidgets.QTableWidgetItem()
        self.setItem(row, column, item)
        self.item(row, column).setText(value)
    def addCheckCell(self, row: int, column: int, value: str = ''):
        item = checkItem(False)
        self.setItem(row, column, item)
        self.item(row, column).setText(value)

class checkItem(QtWidgets.QTableWidgetItem):
    def __init__(self, state: bool = False):
        QtWidgets.QTableWidgetItem.__init__(self)
        print('a')
        self.setCheckState(False)
        print('b')
        connect_icon = QIcon(QPixmap('resurces/connects/connect.png'))
        disconnect_icon = QIcon(QPixmap('resurces/connects/disconnect.png'))
        if state:
            self.setIcon(connect_icon)
        else:
            self.setIcon(disconnect_icon)
