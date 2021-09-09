import threading
from time import sleep
from typing import List
from datetime import date, datetime
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from reportlab.pdfgen import canvas as pdf_canvas
from reportlab.pdfbase import ttfonts, pdfmetrics
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import letter, A4
from Meters.Device import Device
from Meters.AbstractDevices import AbstractObserver
from Meters.Drivers.G7M50Driver import G7M50Driver
from Meters.Drivers.SK4MDriver import SK4MDriver
from models.singelton import singleton
from Meters.Drivers.AbstractDriver import AbstractDriver
from Controllers.GUIController import GUIController
from Enums import DeviceName
import pyvisa as visa
import UI.WindowInicilizer


@singleton
class MeterInit:

    def __init__(self):
        self.__observers: List[AbstractObserver] = []
        self.rm = visa.ResourceManager()
        self.devices: dict = {}
        self.drivers_init()
        gui_controller = GUIController()
        self.attach(gui_controller)

    def drivers_init(self):
        self.devices[DeviceName.spectrum_analizer] = Device(SK4MDriver())
        self.devices[DeviceName.generator] = Device(G7M50Driver())

    def add_device(self, driver: AbstractDriver):
        try:
            device = Device(driver)
            self.devices[device.name] = device
            device.notify()
        except BaseException:
            self.__error('Ошибка драйвера')

    def update_model(self, key: DeviceName, state: bool, ip: str, port: str):
        self.devices[key].port = port
        self.devices[key].ip = ip
        result = self.devices[key].connect(state)
        if result != 'Success':
            self.__error(result)

    def attach(self, observer: AbstractObserver):
        self.__observers.append(observer)
        for item in self.devices.values():
            item.attach(observer)

    def start_measure(self):
        for device in self.devices.values():
            device.start()
        self.__check_thread = threading.Thread(target=self.__check_measure, daemon=True)
        self.__check_thread.start()

    def stop_measure(self):
        for device in self.devices.values():
            device.stop()

    def save_report(self):
        save_file_dialog = QFileDialog.getSaveFileName(filter='*.pdf', directory=f'/report_{str(date.today())}')[0]
        if save_file_dialog != '':
            print(save_file_dialog)
            left = 20 * mm
            from models.Parcel_model import Parcel
            parcel = Parcel()
            UI.WindowInicilizer.mainWindow.parcelWidget.safe_as_png('temp/report.png')
            font = ttfonts.TTFont('DejaVu', 'DejaVuSansCondensed.ttf')
            pdfmetrics.registerFont(font)
            canvas = pdf_canvas.Canvas(save_file_dialog, pagesize=A4)
            canvas.setFont('DejaVu', 14)
            canvas.translate(mm, mm)
            canvas.drawCentredString(105 * mm, 280 * mm, f'Отчет №___ от {date.today()}')
            canvas.drawString(left, 270 * mm, text=f'Рабочая частота {parcel.frequency} ГГц')
            canvas.drawString(left, 260 * mm, text=f'Диапазон мощности {parcel.power[1]}...{parcel.power[0]} ДБм')
            canvas.drawString(left, 250 * mm, text=f'Число посылок {parcel.signal_count}')
            canvas.drawImage('temp/report.png', x=0 * mm, y=140 * mm, height=100 * mm, width=210 * mm)
            canvas.drawCentredString(105 * mm, 125 * mm, f'{date.today()}')
            canvas.line(left, 120 * mm, 190 * mm, 120 * mm)
            canvas.setFont('DejaVu', 9)
            canvas.drawString(left, 115 * mm, text=f'Измерения провел')
            canvas.drawCentredString(105 * mm, 115 * mm, f'дата')
            canvas.drawString(170 * mm, 115 * mm, text=f'подпись')
            canvas.save()

    def __check_measure(self):
        while self.devices[DeviceName.generator].driver.is_measure_active:
            sleep(0.1)
        self.stop_measure()

    def __error(self, message):
        self.message = QMessageBox()
        self.message.setWindowTitle('Ошибка')
        self.message.setText(message)
        self.message.setIcon(QMessageBox.Critical)
        self.message.show()

