from Inicilizer import WindowInicilizer
from UI import MainPage
from UI import Events

if __name__ == '__main__':
    mainWindow = MainPage.Ui_MainWindow()
    windowInicilizer = WindowInicilizer.WindowCreate
    connects = Events.Connects
    windowInicilizer.render(mainWindow,connects.mainPage)
