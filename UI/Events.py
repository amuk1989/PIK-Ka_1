from UI import MainPage
from Test import SHowMessage

class Events(MainPage.Ui_MainWindow):
    def __init__(self):
        super().OpenFileButton.clicked.connect(SHowMessage.Say)

#self.optionsButton.clicked.connect(SHowMessage.Say)
#self.optionsButton_1.clicked.connect(SHowMessage.Say)
#self.safeFileButton.clicked.connect(SHowMessage.Say)