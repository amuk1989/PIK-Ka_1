from typing import List

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel

class QSwitch(QWidget):
    __img_r = 'resurces/slider.png'
    __img_l = 'resurces/slider_l.png'
    __size = QSize(69, 45)
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.lbl = QLabel(self)
        self.lbl.setAlignment(Qt.AlignCenter)

        self.hbox = QHBoxLayout(self)
        self.lbl.resize(self.__size)
        self.hbox.addWidget(self.lbl)
        self.setLayout(self.hbox)

        self.__right_objects: List[QWidget] = []
        self.__left_objects: List[QWidget] = []
        self.state = False
        self.draw()

    def draw(self):
        if self.state:
            pixmap = QPixmap(self.__img_r).scaled(self.__size, aspectRatioMode = Qt.KeepAspectRatio)
        else:
            pixmap = QPixmap(self.__img_l).scaled(self.__size, aspectRatioMode = Qt.KeepAspectRatio)
        self.lbl.setPixmap(pixmap)
        self.show()

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            self.state = not self.state
            if self.__right_objects[0] != None:
                self.__set_enabled(self.__right_objects, self.state)
            if self.__left_objects[0] != None:
                self.__set_enabled(self.__left_objects, not self.state)
            self.draw()

    def right_position_connect(self, subject: QWidget):
        self.__right_objects.append(subject)
        self.__set_enabled(self.__right_objects, self.state)

    def left_position_connect(self, subject: QWidget):
        self.__left_objects.append(subject)
        self.__set_enabled(self.__left_objects, not self.state)

    def __set_enabled(self, objects: List[QWidget], enable: bool):
        for object in objects:
            object.setEnabled(enable)