from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from models.AbstractParcel import AbstractParcel
from models.MarkerModel import marker_model
from typing import List
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton

class GraphicsWiget(QWidget):
    __mousePos_x: float
    __mousePos_y: float
    __markers_indexes: List[int] = []
    __subject: AbstractParcel
    __focus_marker: marker_model

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.__focus_marker = marker_model()

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)
        self.canvas.mpl_connect('motion_notify_event', self.on_move)
        self.canvas.mpl_connect('button_press_event', self.on_click)

    @pyqtSlot()
    def drawAmp(self, subject: AbstractParcel):

        self.__subject = subject

        self.x_axis = list(self.__subject.set_graph().keys())
        self.y_axis = list(self.__subject.set_graph().values())

        for i in range (0, len(self.__subject.get_markers())):
            self.__markers_indexes.append(self.__subject.get_markers()[i].marker_index)

        self.update()

    def update(self, marker_index:int = None):

        self.canvas.axes.clear()
        self.canvas.axes.plot(self.x_axis, self.y_axis, 'o', ls='-', ms=4, markevery=self.__markers_indexes)

        if marker_index != None:
            self.__focus_marker.marker_index = marker_index
            self.canvas.axes.scatter(self.x_axis[marker_index], self.y_axis[marker_index])
        else:
            self.__focus_marker.marker_index = None

        self.canvas.draw()

    def on_move(self,event):
        x, y = event.x, event.y
        if event.inaxes:
            ax = event.inaxes  # the axes instance
            self.__mousePos_x = event.xdata
            self.__mousePos_y = event.ydata
            self.find_marker()

    def on_click(self,event):
        if self.__focus_marker.marker_index!=None:
            self.__subject.add_marker(self.__focus_marker)

    def find_marker(self):
        distance: List[float] = []
        for i in range (0, len(self.x_axis)):
            distance.append(math.hypot(self.x_axis[i]-self.__mousePos_x, self.y_axis[i]-self.__mousePos_y))
        result = np.argmin(np.abs(distance))
        if distance[result] < 1:

            self.update(result)
        else:

            self.update()