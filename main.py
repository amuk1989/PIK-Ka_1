from Inicilizer import WindowInicilizer
from UI import MainPage, optionPage
from UI import Events


class main():
    @staticmethod
    def optionPage():
        return optionPage.Ui_optionPage()

    @staticmethod
    def windowInicilizer():
        return WindowInicilizer.WindowCreate()

    @staticmethod
    def connects():
        return Events.Connects()

if __name__ == '__main__':
    mainWindow = MainPage.Ui_MainWindow()
    main.windowInicilizer().render(mainWindow, Events.Connects.mainPage)

