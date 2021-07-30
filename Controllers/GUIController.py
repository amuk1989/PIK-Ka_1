import Enums
from Meters.Device import Device
from models.AbstractParcel import AbstractParcelObserver, AbstractParcel
from Meters.AbstractDevices import AbstractObserver
from models.singelton import singleton


@singleton
class GUIController(AbstractParcelObserver, AbstractObserver):
    def update(self, subject: AbstractParcel):
        if str(subject) == 'Parcel':
            from UI.WindowInicilizer import mainWindow, optionWindow
            mainWindow.timeEdit.setValue(subject.detonation_time)
            optionWindow.timeEdit.setValue(subject.detonation_time)
            mainWindow.modeBox.setCurrentIndex(subject.parcel_mode)
            optionWindow.modeBox.setCurrentIndex(subject.parcel_mode)
            mainWindow.parcelCountBox.setValue(subject.signal_count)

    def update_from_device(self, subject: Device):
        from UI.WindowInicilizer import mainWindow
        if subject.name == Enums.DeviceName.spectrum_analizer:
            mainWindow.frequencyMinBox.setValue(subject.driver.min_range)
            mainWindow.frequencyMaxBox.setValue(subject.driver.max_range)
            mainWindow.dotsCountBox.setValue(subject.driver.dots_count_range)

    def update_from_generator(self, power: float, frequency: float):
        from UI.WindowInicilizer import mainWindow
        mainWindow.earthPowerLabel.setText(str(power))
        mainWindow.signalFrequencyLabel.setText(str(frequency))
