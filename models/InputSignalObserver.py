from models.AbstractParcel import AbstractParcelObserver,AbstractParcel

class input_signal_observer(AbstractParcelObserver):
    def update(self, subject: AbstractParcel):
        from UI.WindowInicilizer import mainWindow
        mainWindow.FRWidget.drawAmp(subject.get_graph(),subject.get_markers())