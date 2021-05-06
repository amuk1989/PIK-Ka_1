from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import pyqtSlot
from matplotlib.figure import Figure
import random
import numpy as np
from Meters.MeterPNA.MeterPNA import MeterPNA

class GraphicsWiget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

    @pyqtSlot()
    def update_graph(self):


        fs = 500
        f = random.randint(1, 100)
        ts = 1 / fs
        length_of_signal = 100
        t = np.linspace(0, 1, length_of_signal)

        cosinus_signal = np.cos(2 * np.pi * f * t)
        sinus_signal = np.sin(2 * np.pi * f * t)

        self.canvas.axes.clear()
        self.canvas.axes.plot(t, cosinus_signal, marker="o", ms=4)
        self.canvas.axes.plot(t, sinus_signal, marker="o", ms=4)

        self.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
        self.canvas.axes.set_title('Cosinus - Sinus Signal')
        self.canvas.draw()

    @pyqtSlot()
    def drawAmp(self):

        self.meter.Measure()
        data = self.meter.Fetch()

        x_axis = np.linspace(0, len(data), len(data))
        dataReal =[]
        dataPh = []
        for i in range(len(data)):
            dataReal.append(data[i].real)
            dataPh.append(data[i].imag)

        self.canvas.axes.clear()
        self.canvas.axes.plot(x_axis, dataReal)
        self.canvas.draw()


