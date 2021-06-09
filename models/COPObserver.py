from models.AbstractParcel import AbstractParcelObserver,AbstractParcel

class COP_observer(AbstractParcelObserver):
    def update(self, subject: AbstractParcel):
        from UI.WindowInicilizer import mainWindow,optionWindow
        mainWindow.COPwidget.drawAmp(subject.get_graph(), subject.get_mask(), subject.get_markers(), subject.get_label())
        mainWindow.COPwidget.setEnabled(True)