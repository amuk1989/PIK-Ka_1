from models.AbstractParcel import AbstractParcelObserver,AbstractParcel

class ParcelObserver(AbstractParcelObserver):
    def update(self, subject: AbstractParcel):
        from UI.WindowInicilizer import mainWindow
        mainWindow.parcelWidget.drawAmp(subject.get_graph(),subject.get_mask(), subject.get_markers(), subject.get_label())
        mainWindow.parcelWidget.setEnabled(True)
