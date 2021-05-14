from UI.WindowInicilizer import mainWindow,optionWindow
from models.AbstractParcel import AbstractParcelObserver, AbstractParcel

class GUIController(AbstractParcelObserver):
    def update(self, subject: AbstractParcel):
        pass