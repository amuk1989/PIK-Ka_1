# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setStyleSheet("font: 87 10pt \"Gilroy\";")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chartsTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.chartsTabs.setGeometry(QtCore.QRect(0, 60, 1027, 571))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chartsTabs.sizePolicy().hasHeightForWidth())
        self.chartsTabs.setSizePolicy(sizePolicy)
        self.chartsTabs.setTabletTracking(False)
        self.chartsTabs.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.chartsTabs.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chartsTabs.setTabPosition(QtWidgets.QTabWidget.South)
        self.chartsTabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.chartsTabs.setIconSize(QtCore.QSize(16, 16))
        self.chartsTabs.setObjectName("chartsTabs")
        self.frequencyResponceTab = QtWidgets.QWidget()
        self.frequencyResponceTab.setObjectName("frequencyResponceTab")
        self.chartsTabs.addTab(self.frequencyResponceTab, "")
        self.probabilityOfProgrammingTab = QtWidgets.QWidget()
        self.probabilityOfProgrammingTab.setObjectName("probabilityOfProgrammingTab")
        self.chartsTabs.addTab(self.probabilityOfProgrammingTab, "")
        self.sensitivityTab = QtWidgets.QWidget()
        self.sensitivityTab.setObjectName("sensitivityTab")
        self.chartsTabs.addTab(self.sensitivityTab, "")
        self.parcelTab = QtWidgets.QWidget()
        self.parcelTab.setObjectName("parcelTab")
        self.graphicsView = QtWidgets.QGraphicsView(self.parcelTab)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1021, 551))
        self.graphicsView.setObjectName("graphicsView")
        self.chartsTabs.addTab(self.parcelTab, "")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1024, 65))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setToolTip("")
        self.tabWidget.setToolTipDuration(0)
        self.tabWidget.setStatusTip("")
        self.tabWidget.setWhatsThis("")
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(100, 25))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.fileTab = QtWidgets.QWidget()
        self.fileTab.setMaximumSize(QtCore.QSize(801, 48))
        self.fileTab.setObjectName("fileTab")
        self.OpenFileButton = QtWidgets.QCommandLinkButton(self.fileTab)
        self.OpenFileButton.setGeometry(QtCore.QRect(0, 0, 128, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenFileButton.sizePolicy().hasHeightForWidth())
        self.OpenFileButton.setSizePolicy(sizePolicy)
        self.OpenFileButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.OpenFileButton.setAutoFillBackground(False)
        self.OpenFileButton.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resurces/MainTab/NewFile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OpenFileButton.setIcon(icon)
        self.OpenFileButton.setIconSize(QtCore.QSize(25, 25))
        self.OpenFileButton.setObjectName("OpenFileButton")
        self.safeFileButton = QtWidgets.QCommandLinkButton(self.fileTab)
        self.safeFileButton.setGeometry(QtCore.QRect(128, 0, 144, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.safeFileButton.sizePolicy().hasHeightForWidth())
        self.safeFileButton.setSizePolicy(sizePolicy)
        self.safeFileButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.safeFileButton.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resurces/MainTab/SaveFile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.safeFileButton.setIcon(icon1)
        self.safeFileButton.setIconSize(QtCore.QSize(25, 25))
        self.safeFileButton.setObjectName("safeFileButton")
        self.tabWidget.addTab(self.fileTab, "Файл")
        self.measurenceTab = QtWidgets.QWidget()
        self.measurenceTab.setObjectName("measurenceTab")
        self.startButton = QtWidgets.QCommandLinkButton(self.measurenceTab)
        self.startButton.setGeometry(QtCore.QRect(0, 0, 72, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resurces/MainTab/Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon2)
        self.startButton.setObjectName("startButton")
        self.optionsButton = QtWidgets.QCommandLinkButton(self.measurenceTab)
        self.optionsButton.setGeometry(QtCore.QRect(72, 0, 176, 41))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resurces/MainTab/options.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.optionsButton.setIcon(icon3)
        self.optionsButton.setObjectName("optionsButton")
        self.connectOptionsButton = QtWidgets.QCommandLinkButton(self.measurenceTab)
        self.connectOptionsButton.setGeometry(QtCore.QRect(248, 0, 191, 41))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resurces/MainTab/Connect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connectOptionsButton.setIcon(icon4)
        self.connectOptionsButton.setObjectName("connectOptionsButton")
        self.optionsButton_2 = QtWidgets.QCommandLinkButton(self.measurenceTab)
        self.optionsButton_2.setGeometry(QtCore.QRect(260, 40, 176, 41))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("C:/Users/User/.designer/backup/resurces/MainTab/options.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.optionsButton_2.setIcon(icon5)
        self.optionsButton_2.setObjectName("optionsButton_2")
        self.tabWidget.addTab(self.measurenceTab, "")
        self.optionsTab = QtWidgets.QWidget()
        self.optionsTab.setObjectName("optionsTab")
        self.optionsButton_1 = QtWidgets.QCommandLinkButton(self.optionsTab)
        self.optionsButton_1.setGeometry(QtCore.QRect(0, 0, 176, 41))
        self.optionsButton_1.setIcon(icon3)
        self.optionsButton_1.setObjectName("optionsButton_1")
        self.connectOptionsButton_1 = QtWidgets.QCommandLinkButton(self.optionsTab)
        self.connectOptionsButton_1.setGeometry(QtCore.QRect(176, 0, 191, 41))
        self.connectOptionsButton_1.setIcon(icon4)
        self.connectOptionsButton_1.setObjectName("connectOptionsButton_1")
        self.tabWidget.addTab(self.optionsTab, "")
        self.chartsTab = QtWidgets.QWidget()
        self.chartsTab.setObjectName("chartsTab")
        self.addMarkerButton = QtWidgets.QCommandLinkButton(self.chartsTab)
        self.addMarkerButton.setGeometry(QtCore.QRect(0, 0, 146, 41))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resurces/MainTab/AddMarker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addMarkerButton.setIcon(icon6)
        self.addMarkerButton.setObjectName("addMarkerButton")
        self.tabWidget.addTab(self.chartsTab, "")
        self.helpTab = QtWidgets.QWidget()
        self.helpTab.setObjectName("helpTab")
        self.helpButton = QtWidgets.QCommandLinkButton(self.helpTab)
        self.helpButton.setGeometry(QtCore.QRect(0, 0, 88, 41))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("resurces/MainTab/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpButton.setIcon(icon7)
        self.helpButton.setObjectName("helpButton")
        self.tabWidget.addTab(self.helpTab, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 640, 131, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 710, 21, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 640, 131, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 710, 21, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(316, 640, 121, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(360, 710, 21, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 640, 121, 31))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(510, 710, 21, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(610, 640, 131, 31))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(890, 640, 101, 31))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.responseTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.responseTimeLabel.setGeometry(QtCore.QRect(60, 670, 21, 41))
        self.responseTimeLabel.setStyleSheet("font: 20pt \"a_LCDNova\";")
        self.responseTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.responseTimeLabel.setObjectName("responseTimeLabel")
        self.earthPowerLabel = QtWidgets.QLabel(self.centralwidget)
        self.earthPowerLabel.setGeometry(QtCore.QRect(210, 670, 21, 41))
        self.earthPowerLabel.setStyleSheet("font: 20pt \"a_LCDNova\";")
        self.earthPowerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.earthPowerLabel.setObjectName("earthPowerLabel")
        self.signalFrequencyLabel = QtWidgets.QLabel(self.centralwidget)
        self.signalFrequencyLabel.setGeometry(QtCore.QRect(360, 670, 21, 41))
        self.signalFrequencyLabel.setStyleSheet("font: 20pt \"a_LCDNova\";")
        self.signalFrequencyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.signalFrequencyLabel.setObjectName("signalFrequencyLabel")
        self.createParcelTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.createParcelTimeLabel.setGeometry(QtCore.QRect(510, 670, 21, 41))
        self.createParcelTimeLabel.setStyleSheet("font: 20pt \"a_LCDNova\";")
        self.createParcelTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.createParcelTimeLabel.setObjectName("createParcelTimeLabel")
        self.parcelCountLabel = QtWidgets.QLabel(self.centralwidget)
        self.parcelCountLabel.setGeometry(QtCore.QRect(660, 670, 21, 41))
        self.parcelCountLabel.setStyleSheet("font: 20pt \"a_LCDNova\";")
        self.parcelCountLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.parcelCountLabel.setObjectName("parcelCountLabel")
        self.onTimerLabel = QtWidgets.QLabel(self.centralwidget)
        self.onTimerLabel.setGeometry(QtCore.QRect(885, 670, 111, 41))
        self.onTimerLabel.setStyleSheet("font: 20pt \"a_LCDNova\";")
        self.onTimerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.onTimerLabel.setObjectName("onTimerLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.chartsTabs.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ПИК-Ка"))
        self.chartsTabs.setTabText(self.chartsTabs.indexOf(self.frequencyResponceTab), _translate("MainWindow", "АЧХ"))
        self.chartsTabs.setTabText(self.chartsTabs.indexOf(self.probabilityOfProgrammingTab), _translate("MainWindow", "Вероятность программирования"))
        self.chartsTabs.setTabText(self.chartsTabs.indexOf(self.sensitivityTab), _translate("MainWindow", "Чувствительность"))
        self.chartsTabs.setTabText(self.chartsTabs.indexOf(self.parcelTab), _translate("MainWindow", "Кодовая импульсная посылка"))
        self.OpenFileButton.setText(_translate("MainWindow", "Открыть файл"))
        self.safeFileButton.setText(_translate("MainWindow", "Сохранить файл"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.optionsButton.setText(_translate("MainWindow", "Настройки измерений"))
        self.connectOptionsButton.setText(_translate("MainWindow", "Настройки подключений"))
        self.optionsButton_2.setText(_translate("MainWindow", "Настройки измерений"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.measurenceTab), _translate("MainWindow", "Измерения"))
        self.optionsButton_1.setText(_translate("MainWindow", "Настройки измерений"))
        self.connectOptionsButton_1.setText(_translate("MainWindow", "Настройки подключений"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.optionsTab), _translate("MainWindow", "Настройки"))
        self.addMarkerButton.setText(_translate("MainWindow", "Добавить маркер"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chartsTab), _translate("MainWindow", "Графики"))
        self.helpButton.setText(_translate("MainWindow", "Справка"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.helpTab), _translate("MainWindow", "Помощь"))
        self.label.setText(_translate("MainWindow", "Время срабатывания"))
        self.label_2.setText(_translate("MainWindow", "мс"))
        self.label_3.setText(_translate("MainWindow", "Мощность\n"
"подситемы \"Земля\""))
        self.label_4.setText(_translate("MainWindow", "кВт"))
        self.label_5.setText(_translate("MainWindow", "Частота сигнала\n"
"п/с КРЛ \"Земля\""))
        self.label_6.setText(_translate("MainWindow", "ГГц"))
        self.label_7.setText(_translate("MainWindow", "Время\n"
"формирования КИП"))
        self.label_8.setText(_translate("MainWindow", "мс"))
        self.label_9.setText(_translate("MainWindow", "Колличество КИП"))
        self.label_10.setText(_translate("MainWindow", "Время работы"))
        self.responseTimeLabel.setText(_translate("MainWindow", "0"))
        self.earthPowerLabel.setText(_translate("MainWindow", "0"))
        self.signalFrequencyLabel.setText(_translate("MainWindow", "0"))
        self.createParcelTimeLabel.setText(_translate("MainWindow", "0"))
        self.parcelCountLabel.setText(_translate("MainWindow", "0"))
        self.onTimerLabel.setText(_translate("MainWindow", "00:00:00"))
