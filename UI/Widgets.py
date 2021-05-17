from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from models.MarkerModel import marker_model
from typing import List
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton

class GraphicsWiget(QWidget):
    __mousePos_x: float = 0
    __mousePos_y: float = 0
    __markers: List[int] = []
    __marker_focus: int = None

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        __mousePos_x: float = 0
        __mousePos_y: float = 0
        #__markers: List[marker_model]

        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)
        self.binding_id = self.canvas.mpl_connect('motion_notify_event', self.on_move)

    @pyqtSlot()
    def drawAmp(self, data, markers = []):

        self.x_axis = list(data.keys())
        self.y_axis = list(data.values())

        self.update()

    def update(self, marker_index:int = None):

        self.canvas.axes.clear()
        self.canvas.axes.plot(self.x_axis, self.y_axis, 'o', ls='-', ms=4, markevery=self.__markers)

        if marker_index != None:
            self.canvas.axes.scatter(self.x_axis[marker_index], self.y_axis[marker_index])
        self.canvas.draw()

    def on_move(self,event):
        x, y = event.x, event.y
        if event.inaxes:
            ax = event.inaxes  # the axes instance
            self.__mousePos_x = event.xdata
            self.__mousePos_y = event.ydata
            self.find_marker()

    def find_marker(self):
        distance: List[float] = []
        for i in range (0, len(self.x_axis)):
            distance.append(math.hypot(self.x_axis[i]-self.__mousePos_x, self.y_axis[i]-self.__mousePos_y))
        result = np.argmin(np.abs(distance))
        if distance[result] < 1:
            self.update(result)