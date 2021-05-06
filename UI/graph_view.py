import numpy
import matplotlib.pyplot as pyplot
from UI.WindowInicilizer import mainWindow

pyplot.ioff()

for i in range(3):
    pyplot.plot(numpy.random.rand(10))


mainWindow.graphicsView.setScene(pyplot)
pyplot.show()