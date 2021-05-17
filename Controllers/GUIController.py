from UI.Widgets import GraphicsWiget
from models.AbstractParcel import AbstractParcelObserver, AbstractParcel

class GUIController(AbstractParcelObserver):
    def __init__(self, widget: GraphicsWiget):
        pass

    def update(self, subject: AbstractParcel):
        pass