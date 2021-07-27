from typing import List, Any
from Controllers.InputSignalController import inputSignalController
from Controllers.ParcelController import Parcel_controller
from Controllers.GUIController import GUIController
from models.MarkerModel import marker_model
from models.singelton import singleton


@singleton
class Client:
    def __init__(self):
        self.input_controller = inputSignalController()
        self.parcel_controller = Parcel_controller()
        self.gui_controller = GUIController()
        self.input_controller.set_next(self.parcel_controller)
        self.parcel_controller.set_next(self.gui_controller)

    def add_marker(self, object_name: str, marker: marker_model):
        self.input_controller.add_marker(object_name, marker)

    def insert_marker(self, object_name: str, i: int, markers: List[marker_model]):
        self.input_controller.insert_marker(object_name, i, markers)

    def delete_marker(self, request: Any, marker: marker_model):
        self.input_controller.delete_marker(request, marker)
