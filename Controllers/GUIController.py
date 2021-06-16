from models.AbstractParcel import AbstractParcelObserver, AbstractParcel
from models.singelton import singleton

@singleton
class GUIController(AbstractParcelObserver):
    def __init__(self):
        pass#self.connects()
    def update(self, subject: AbstractParcel):
        if str(subject) == 'Parcel':
            from UI.WindowInicilizer import mainWindow, optionWindow
            mainWindow.timeEdit.setValue(subject.detonation_time)
            optionWindow.timeEdit.setValue(subject.detonation_time)
            mainWindow.modeBox.setCurrentIndex(subject.parcel_mode)
            optionWindow.modeBox.setCurrentIndex(subject.parcel_mode)
