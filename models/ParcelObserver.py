from models.AbstractParcel import AbstractParcelObserver,AbstractParcel

class ParcelObserver(AbstractParcelObserver):
    def update(self, subject: AbstractParcel):
        print(subject)
        from UI.WindowInicilizer import mainWindow,optionWindow
        mainWindow.parcelWidget.drawAmp(subject.set_graph())
        mainWindow.timeEdit.setText(str(subject.detonation_time))
        optionWindow.timeEdit.setText(str(subject.detonation_time))
        mainWindow.modeBox.setCurrentIndex(subject.parcel_mode)
        optionWindow.modeBox.setCurrentIndex(subject.parcel_mode)
