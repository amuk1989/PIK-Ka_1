from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from models.MarkerModel import marker_model
from typing import List
from Controllers.ParcelController import Parcel_controller
from Controllers.InputSignalController import inputSignalController
from floatMethods import equal
import numpy as np
import math

class GraphicsWiget(QWidget):
    input_signal_controller = inputSignalController()
    parcel_controller = Parcel_controller()
    __markers_x: List[float]
    __markers_y: List[float]
    __markers_legend: List[str]
    __zoom:float

    def __init__(self, parent=None):
        self.input_signal_controller.set_next(self.parcel_controller)

        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())
        self.__focus_marker = marker_model()
        self.__markers_x = []
        self.__markers_y = []
        self.__markers_legend = []
        self.__zoom = 0
        self.__right_lim: float = None

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

        self.canvas.mpl_connect('motion_notify_event', self.mouse_move)
        self.canvas.mpl_connect('button_press_event', self.mouse_click)
        self.canvas.mpl_connect('scroll_event', self.mouse_scroll)

    @pyqtSlot()
    def drawAmp(self, data:dict, legend_mask: str = 'Маркер №, X, Y', markers: marker_model = []):

        flag = False
        self.mask = legend_mask.split(', ')

        self.__x_axis = list(data.keys())
        self.__y_axis = list(data.values())

        for i in range(0, len(markers)):
            if not equal(self.__x_axis, markers[i].x, 2) or not equal(self.__y_axis, markers[i].y, 2):
                markers[i] = self.find_marker(math.inf, markers[i].x)
                flag = True

        if flag:
            self.input_signal_controller.insert_marker(self.objectName(), i, markers)

        self.__markers_y.clear()
        self.__markers_x.clear()
        self.__markers_legend.clear()

        for i in range(0, len(markers)):
            self.__markers_x.append(markers[i].x)
            self.__markers_y.append(markers[i].y)
            self.__markers_legend.append(markers[i].legend)

        self.min_y = np.amin(self.__y_axis)
        self.min_x = np.amin(self.__x_axis)
        self.max_y = np.amax(self.__y_axis)
        self.max_x = np.amax(self.__x_axis)

        if self.__right_lim == None:
            self.__right_lim = self.max_x
            self.__left_lim = self.min_x

        self.update()

    def update(self):
        self.canvas.axes.clear()
        self.canvas.axes.plot(self.__x_axis, self.__y_axis, ls='-')

        if self.__focus_marker != None:
            self.canvas.axes.scatter(self.__focus_marker.x, self.__focus_marker.y)

        self.canvas.axes.scatter(self.__markers_x, self.__markers_y)

        for i in range(0,len(self.__markers_x)):
            self.__marker_draw(self.__markers_x[i], self.__markers_y[i])

        self.canvas.axes.set_xlim(self.__left_lim, self.__right_lim)
        self.canvas.draw()

    #region events
    def mouse_move(self,event):
        last_marker: marker_model
        x, y = event.x, event.y
        if event.inaxes:
            ax = event.inaxes  # the axes instance
            self.__focus_marker = self.find_marker(1, event.xdata, event.ydata)
            self.update()

    def mouse_click(self, event):
        x, y = event.x, event.y
        if event.inaxes:
            ax = event.inaxes  # the axes instance
            if self.__focus_marker != None:
                self.input_signal_controller.add_marker(self.objectName(),self.__focus_marker)

    def mouse_scroll(self,event):
        if event.inaxes:
            x, y = event.xdata, event.ydata
            left, right = self.size_canvas(x,y,self.__right_lim,self.max_y,self.__left_lim,self.min_y)

            if self.__left_lim >= 0:
                self.__left_lim += event.step*left
            else:
                self.__left_lim = 0

            if self.__right_lim <= self.max_x:
                self.__right_lim += event.step*right
            else:
                self.__right_lim = self.max_x

            self.update()

    #endregion


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

    def __marker_draw(self, marker_x: float, marker_y: float):
        self.canvas.axes.plot([marker_x, self.min_x + self.__left_lim], [marker_y, marker_y],
                              color='black', dashes=[6, 4], linewidth=0.5)

        self.canvas.axes.annotate(f'{self.mask[0]} \n{self.mask[2]}:{round(marker_y, 2)}',
                                  xy=(self.min_x + self.__left_lim, marker_y), xycoords='data',
                                  xytext=(-60,-7), textcoords='offset points',
                                  bbox=dict(boxstyle="round", fc="0.8"),
                                  arrowprops=dict(arrowstyle="-")
                                  )

        self.canvas.axes.plot([marker_x, marker_x], [marker_y, self.min_y],
                              color='black', dashes=[6, 4], linewidth=0.5)

        self.canvas.axes.annotate(f'{self.mask[0]} \n{self.mask[1]}:{round(marker_x, 2)}',
                                    xy=(marker_x, self.min_y), xycoords='data',
                                    xytext=(0, -25), textcoords='offset points',
                                    bbox=dict(boxstyle="round", fc="0.8"),
                                    arrowprops=dict(arrowstyle="-",
                                    connectionstyle="angle,angleA=0,angleB=90,rad=10"))

    def size_canvas(self,x_mouse: float,y_mouse: float, x_max:float, y_max:float, x_min:float, y_min:float):
        right_x = (1/(x_max-x_min)) * (x_max - x_mouse)
        left_x = (1/(x_max-x_min)) * (x_min - x_mouse)
        return left_x, right_x
