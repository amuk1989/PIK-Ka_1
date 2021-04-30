from UI import MainPage
from UI.Test import Message

class Connects(MainPage.Ui_MainWindow):
    def __init__(self):
        pass

    def mainPage(page):
        page.optionsButton.clicked.connect(Message.Say)

    def optionPage(page):
        page.OkButton.clicked.connect(Message.Say)


#self.optionsButton.clicked.connect(SHowMessage.Say)
#self.optionsButton_1.clicked.connect(SHowMessage.Say)
#self.safeFileButton.clicked.connect(SHowMessage.Say)