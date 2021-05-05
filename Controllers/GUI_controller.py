from Inicilizer.WindowInicilizer import optionWindow
from models.Parcel_model import parcel

class GUI_conroller(object):
    def __init__(self):
        optionWindow.modeBox.itemText(parcel.parcel_mode)