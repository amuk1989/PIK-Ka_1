from PyQt5 import QtGui
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel


class QSwitch(QWidget):
    state = False
    __right_object: QWidget
    __left_object: QWidget
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.hbox = QHBoxLayout(self)
        self.lbl = QLabel(self)
        self.lbl.setAlignment(Qt.AlignCenter)
        self.__object = None
        self.draw()
    def draw(self):
        if self.state:
            img = 'resurces/slider.png'
        else:
            img = 'resurces/slider_l.png'
        self.resize(40, 40)
        self.lbl.resize(self.size())
        pixmap = QPixmap(img).scaled(self.lbl.size(), aspectRatioMode = Qt.KeepAspectRatioByExpanding)
        self.lbl.setPixmap(pixmap)
        self.hbox.addWidget(self.lbl)
        self.setLayout(self.hbox)
        self.show()

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            self.state = not self.state
            if self.__right_object != None:
                self.__right_object.setEnabled(self.state)
            if self.__left_object != None:
                self.__left_object.setEnabled(not self.state)
            self.draw()

    def right_position_connect(self, subject: QWidget):
        self.__right_object = subject
        self.__right_object.setEnabled(self.state)

    def left_position_connect(self, subject: QWidget):
        self.__left_object = subject
        self.__left_object.setEnabled(not self.state)