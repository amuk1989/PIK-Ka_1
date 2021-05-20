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
    __markers_x: List[float]
    __markers_y: List[float]
    __markers_legend: List[str]
    def __init__(self, parent=None):
        self.input_signal_controller.set_next(self.parcel_controller)

        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())
        self.__focus_marker = marker_model()
        self.__markers_x = []
        self.__markers_y = []
        self.__markers_legend = []

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

        self.canvas.mpl_connect('motion_notify_event', self.mouse_move)
        self.canvas.mpl_connect('button_press_event', self.mouse_click)

    @pyqtSlot()
    def drawAmp(self, data:dict, markers :marker_model = []):
        flag = False

        self.__markers_y.clear()
        self.__markers_x.clear()
        self.__markers_legend.clear()

        self.__x_axis = list(data.keys())
        self.__y_axis = list(data.values())

        for i in range(0, len(markers)):
            if not self.__x_axis.count(markers[i].x) or not self.__y_axis.count(markers[i].y):
                markers[i] = self.find_marker(math.inf, markers[i].x)
                flag = True

        if flag:
            self.input_signal_controller.insert_marker(self.objectName(), i, markers)

        for i in range(0, len(markers)):
            self.__markers_x.append(markers[i].x)
            self.__markers_y.append(markers[i].y)
            self.__markers_legend.append(markers[i].legend)
        self.update()

    def update(self):
        self.canvas.axes.clear()
        self.canvas.axes.plot(self.__x_axis, self.__y_axis, ls='-')

        if self.__focus_marker != None:
            self.canvas.axes.scatter(self.__focus_marker.x, self.__focus_marker.y)

        self.canvas.axes.scatter(self.__markers_x, self.__markers_y)

        for i in range(0,len(self.__markers_x)):
            self.canvas.axes.annotate(self.__markers_legend[i],
                                        xy=(self.__markers_x[i], self.__markers_y[i]), xycoords='data',
                                        xytext=(-60, 30), textcoords='offset points',
                                        bbox=dict(boxstyle="round", fc="0.8"),
                                        arrowprops=dict(arrowstyle="->",
                                        connectionstyle="angle,angleA=0,angleB=90,rad=10"))
        self.canvas.draw()

    def mouse_move(self,event):
        last_marker: marker_model
        x, y = event.x, event.y
        if event.inaxes:
            ax = event.inaxes  # the axes instance
            #self.__mousePos_x = event.xdata
            #self.__mousePos_y = event.ydata
            self.__focus_marker = self.find_marker(1, event.xdata, event.ydata)
            self.update()



    def mouse_click(self, event):
        x, y = event.x, event.y
        if event.inaxes:
            ax = event.inaxes  # the axes instance
            if self.__focus_marker != None:
                self.input_signal_controller.add_marker(self.objectName(),self.__focus_marker)


    def find_marker(self, trap_size: float, x_pos:float,y_pos: float = None) -> marker_model:
        marker = marker_model()
        distance: List[float] = []

        for i in range(0, len(self.__x_axis)):
            if y_pos == None:
                y_pos = self.__y_axis[i]
            distance.append(math.hypot(self.__x_axis[i] - x_pos, self.__y_axis[i] - y_pos))

        result = np.argmin(np.abs(distance))

        if distance[result] < trap_size:
            marker.x = self.__x_axis[result]
            marker.y = self.__y_axis[result]
            return marker
        else:
            return None