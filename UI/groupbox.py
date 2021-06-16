from PyQt5 import QtGui
from PyQt5.QtWidgets import QGroupBox, QWidget


class GroupBox(QGroupBox):
    def __init__(self, parent: QWidget = None):
        QGroupBox.__init__(self, parent)
        self.state = True
        self.setFixedHeight(381)
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        self.state = not self.state
        if self.state:
            self.setFixedHeight(381)
        else:
            self.setFixedHeight(21)
