# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Test import SHowMessage

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chartsTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.chartsTabs.setGeometry(QtCore.QRect(0, 60, 1024, 571))
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
        font.setPointSize(10)
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
        self.tabWidget.setIconSize(QtCore.QSize(30, 15))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
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
        self.OpenFileButton.setAutoFillBackground(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/resurces/MainTab/NewFile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon1.addPixmap(QtGui.QPixmap("UI/resurces/MainTab/SaveFile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.safeFileButton.setIcon(icon1)
        self.safeFileButton.setIconSize(QtCore.QSize(25, 25))
        self.safeFileButton.setObjectName("safeFileButton")
        self.tabWidget.addTab(self.fileTab, "Файл")
        self.measurenceTab = QtWidgets.QWidget()
        self.measurenceTab.setObjectName("measurenceTab")
        self.startButton = QtWidgets.QCommandLinkButton(self.measurenceTab)
        self.startButton.setGeometry(QtCore.QRect(0, 0, 72, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("UI/resurces/MainTab/Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon2)
        self.startButton.setObjectName("startButton")
        self.optionsButton = QtWidgets.QCommandLinkButton(self.measurenceTab)
        self.optionsButton.setGeometry(QtCore.QRect(72, 0, 176, 41))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("UI/resurces/MainTab/options.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.optionsButton.setIcon(icon3)
        self.optionsButton.setObjectName("optionsButton")
        self.connectOptionsButton = QtWidgets.QCommandLinkButton(self.measurenceTab)
        self.connectOptionsButton.setGeometry(QtCore.QRect(248, 0, 191, 41))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("UI/resurces/MainTab/Connect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connectOptionsButton.setIcon(icon4)
        self.connectOptionsButton.setObjectName("connectOptionsButton")
        self.optionsButton_2 = QtWidgets.QCommandLinkButton(self.measurenceTab)
        self.optionsButton_2.setGeometry(QtCore.QRect(260, 40, 176, 41))
        self.optionsButton_2.setIcon(icon3)
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("UI/resurces/MainTab/AddMarker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addMarkerButton.setIcon(icon5)
        self.addMarkerButton.setObjectName("addMarkerButton")
        self.tabWidget.addTab(self.chartsTab, "")
        self.helpTab = QtWidgets.QWidget()
        self.helpTab.setObjectName("helpTab")
        self.helpButton = QtWidgets.QCommandLinkButton(self.helpTab)
        self.helpButton.setGeometry(QtCore.QRect(0, 0, 88, 41))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("UI/resurces/MainTab/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpButton.setIcon(icon6)
        self.helpButton.setObjectName("helpButton")
        self.tabWidget.addTab(self.helpTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.chartsTabs.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.optionsButton.clicked.connect(SHowMessage.Say)
        self.optionsButton_1.clicked.connect(SHowMessage.Say)
        self.safeFileButton.clicked.connect(SHowMessage.Say)

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
