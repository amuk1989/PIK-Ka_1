from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt

class GraphicsWiget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

    @pyqtSlot()
    def drawAmp(self, data, markers = []):

        x_axis = list(data.keys())
        y_axis = list(data.values())

        self.canvas.axes.clear()
        self.canvas.axes.plot(x_axis, y_axis, 'o', ls='-', ms=4, markevery=markers)
        self.canvas.draw()
