from models.AbstractParcel import AbstractParcelObserver,AbstractParcel

class input_signal_observer(AbstractParcelObserver):
    def update(self, subject: AbstractParcel):
        print(subject)
        from UI.WindowInicilizer import mainWindow
        mainWindow.FRWidget.drawAmp(subject.set_graph(),subject.get_markers())