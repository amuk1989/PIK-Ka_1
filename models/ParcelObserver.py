from models.AbstractParcel import AbstractParcelObserver,AbstractParcel

class ParcelObserver(AbstractParcelObserver):
    def update(self, subject: AbstractParcel):
        from UI.WindowInicilizer import mainWindow,optionWindow

        mainWindow.parcelWidget.drawAmp(subject.get_graph(),subject.get_mask(), subject.get_markers())
        mainWindow.timeEdit.setValue(subject.detonation_time)
        optionWindow.timeEdit.setValue(subject.detonation_time)
        mainWindow.modeBox.setCurrentIndex(subject.parcel_mode)
        optionWindow.modeBox.setCurrentIndex(subject.parcel_mode)

        