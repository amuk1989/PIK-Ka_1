from UI import MainPage, optionPage
from UI.Test import Message
from Inicilizer import WindowInicilizer

class Connects(MainPage.Ui_MainWindow):
    def mainPage(page):
        page.optionsButton.clicked.connect(WindowInicilizer.WindowCreate.render(optionPage.Ui_optionPage(),Connects.optionPage))
    def optionPage(page):
        page.OkButton.clicked.connect(Message.Say)


#self.optionsButton.clicked.connect(SHowMessage.Say)
#self.optionsButton_1.clicked.connect(SHowMessage.Say)
#self.safeFileButton.clicked.connect(SHowMessage.Say)