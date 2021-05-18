from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from models.MarkerModel import marker_model
from typing import List
from Controllers.ParcelController import Parcel_controller
from Controllers.InputSignalController import inputSignalController
import numpy as np
import math

class GraphicsWiget(QWidget):
    input_signal_controller = inputSignalController()
    parcel_controller = Parcel_controller()
    def __init__(self, parent=None):
        self.input_signal_controller.set_next(self.parcel_controller)

        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())
        self.__focus_marker = marker_model()

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

        self.canvas.mpl_connect('motion_notify_event', self.mouse_move)
        self.canvas.mpl_connect('button_press_event', self.mouse_click)

    @pyqtSlot()
    def drawAmp(self, data:dict, markers = []):

        self.__x_axis = list(data.keys())
        self.__y_axis = list(data.values())

        self.update()

    def update(self):
        self.canvas.axes.clear()
        self.canvas.axes.plot(self.__x_axis, self.__y_axis, ls='-')
        if self.__focus_marker != None:
            self.canvas.axes.scatter(self.__focus_marker.x, self.__focus_marker.y)
        self.canvas.draw()

    def mouse_move(self,event):
        x, y = event.x, event.y
        if event.inaxes:
            ax = event.inaxes  # the axes instance
            self.__mousePos_x = event.xdata
            self.__mousePos_y = event.ydata
            self.__focus_marker = self.find_marker()
            if self.__focus_marker != None:
                self.update()

    def mouse_click(self, event):
        x, y = event.x, event.y
        if event.inaxes:
            ax = event.inaxes  # the axes instance
            if self.__focus_marker != None:
                self.input_signal_controller.handle(self.objectName(),self.__focus_marker)


    def find_marker(self):
        marker = marker_model()
        distance: List[float] = []
        for i in range(0, len(self.__x_axis)):
            distance.append(math.hypot(self.__x_axis[i] - self.__mousePos_x, self.__y_axis[i] - self.__mousePos_y))
        result = np.argmin(np.abs(distance))
        if distance[result] < 1:
            marker.x = self.__x_axis[result]
            marker.y = self.__y_axis[result]
            return marker
        else:
            return None