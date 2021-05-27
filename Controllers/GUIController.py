from models.AbstractParcel import AbstractParcelObserver, AbstractParcel
from models.singelton import singleton
#from UI.WindowInicilizer import mainWindow, optionWindow

@singleton
class GUIController(AbstractParcelObserver):
    def __init__(self):
        pass#self.connects()
    def update(self, subject: AbstractParcel):
        if str(subject) == 'Parcel':
            from UI.WindowInicilizer import mainWindow, optionWindow
            mainWindow.parcelWidget.drawAmp(subject.get_graph(), subject.get_mask(), subject.get_markers())
            mainWindow.timeEdit.setValue(subject.detonation_time)
            optionWindow.timeEdit.setValue(subject.detonation_time)
            mainWindow.modeBox.setCurrentIndex(subject.parcel_mode)
            optionWindow.modeBox.setCurrentIndex(subject.parcel_mode)

    def connects(self):
        from UI.WindowInicilizer import mainWindow, optionWindow
