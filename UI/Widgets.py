from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from main import parсel

class GraphicsWiget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

    @pyqtSlot()
    def drawAmp(self):
        data = parсel.signal
        x_axis = np.linspace(0, len(data), len(data))
        dataReal = []
        for i in range(len(data)):
            dataReal.append(data[i].real)

        self.canvas.axes.clear()
        self.canvas.axes.plot(x_axis, dataReal)
        self.canvas.draw()