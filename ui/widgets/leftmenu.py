from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt, Slot, Signal
from PySide6.QtSvgWidgets import QSvgWidget

from modules.tempsettings import TempSettings

from modules.backend.serial import listPorts

import resources.resources

class LeftMenu(QtWidgets.QWidget):
    toggleDarkMode = Signal(bool)
    
    closeSerial = Signal()

    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setFixedWidth(250)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)

        self.setObjectName("LeftMenu")

        # Layout
        self.Layout = QtWidgets.QVBoxLayout(self)
        self.Layout.setContentsMargins(15, 10, 15, 10)
        self.Layout.setSpacing(10)
        self.setLayout(self.Layout)

        #QSettings
        self.settings = QtCore.QSettings("DigiLab", "Simulador")
        isDarkMode = self.settings.value("darkMode", defaultValue=TempSettings.get("isDarkModeSystem"), type=bool)

        # Title
        self.SimulationTitle = QtWidgets.QLabel(text="Simulação", parent=self, alignment=QtCore.Qt.AlignCenter)

        # Experiment selection
        self.frameOpenSimulation = QtWidgets.QFrame(self)
        self.frameOpenSimulationLayout = QtWidgets.QHBoxLayout(self.frameOpenSimulation)
        self.frameOpenSimulationLayout.setContentsMargins(0, 0, 0, 0)
        self.frameOpenSimulationLayout.setSpacing(5)

        self.selectSimulation = QtWidgets.QComboBox(self.frameOpenSimulation)
        self.selectSimulation.setCursor(QtCore.Qt.PointingHandCursor)
        self.selectSimulation.setPlaceholderText("Selecionar experimento")
        self.selectSimulation.setFixedHeight(32)

        # self.selectSimulation.clear()

        self.btnOpenSimulation = QtWidgets.QPushButton(parent=self.frameOpenSimulation, icon=QtGui.QIcon(":/images/icons/open.svg"), text="")
        self.btnOpenSimulation.setFixedSize(32, 32)
        self.btnOpenSimulation.setCursor(QtCore.Qt.PointingHandCursor)

        self.frameOpenSimulationLayout.addWidget(self.selectSimulation)
        self.frameOpenSimulationLayout.addWidget(self.btnOpenSimulation)

        # Device selection
        self.frameDevice = QtWidgets.QFrame(self)
        self.frameDeviceLayout = QtWidgets.QHBoxLayout(self.frameDevice)
        self.frameDeviceLayout.setContentsMargins(0, 0, 0, 0)
        self.frameDeviceLayout.setSpacing(5)

        self.selectDevice = QtWidgets.QComboBox(self.frameDevice)
        self.selectDevice.setCursor(QtCore.Qt.PointingHandCursor)
        self.selectDevice.setPlaceholderText("Nenhum disp. encontrado")
        self.selectDevice.setDisabled(True)
        self.selectDevice.setFixedHeight(32)

        # self.selectDevice.currentIndexChanged.connect(self.changeDevice)

        self.updateDevices(True)

        btnUpdateDevicesIcon = QtGui.QIcon(":/images/dark/update.svg" if isDarkMode else ":/images/light/update.svg")
        self.btnUpdateDevices = QtWidgets.QPushButton(parent=self.frameDevice, icon=btnUpdateDevicesIcon, text="")
        self.btnUpdateDevices.setIconSize(QtCore.QSize(18, 18))
        self.btnUpdateDevices.setFixedSize(32, 32)
        self.btnUpdateDevices.setCursor(QtCore.Qt.PointingHandCursor)

        self.btnUpdateDevices.clicked.connect(self.updateDevices)

        self.frameDeviceLayout.addWidget(self.selectDevice)
        self.frameDeviceLayout.addWidget(self.btnUpdateDevices)

        # Simulation controls
        self.SimulationControls = QtWidgets.QFrame(self)
        self.SimulationControls.setObjectName("SimulationControls")
        self.SimulationControlsLayout = QtWidgets.QHBoxLayout(self.SimulationControls)
        self.SimulationControlsLayout.setContentsMargins(0, 0, 0, 0)
        self.SimulationControlsLayout.setSpacing(10)
        self.SimulationControlsLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.btnPlay = QtWidgets.QPushButton(parent=self.SimulationControls, icon=QtGui.QIcon(":/images/icons/play.svg"), text="")
        self.btnPlay.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnPlay.setFixedSize(30, 30)

        self.btnStop = QtWidgets.QPushButton(parent=self.SimulationControls, icon=QtGui.QIcon(":/images/icons/stop.svg"), text="")
        self.btnStop.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnStop.setFixedSize(30, 30)

        self.btnStop.setDisabled(True)

        self.SimulationControlsLayout.addWidget(self.btnPlay)
        self.SimulationControlsLayout.addWidget(self.btnStop)


        # Logo
        self.logoWidget = QtWidgets.QWidget(self)

        self.logoBottom = QSvgWidget(":/images/icons/icon_dark.svg" if isDarkMode else ":/images/icons/icon_light.svg", parent=self)
        self.logoBottom.setFixedSize(120, 120)

        # Footer Bar
        self.footerBar = QtWidgets.QWidget(self)
        self.footerBar.setObjectName("FooterBar")
        self.footerBar.setAttribute(Qt.WA_StyledBackground, True)
        self.footerBar.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        self.footerBarLayout = QtWidgets.QHBoxLayout(self.footerBar)
        self.footerBarLayout.setContentsMargins(10, 10, 10, 0)

        btnDarkModeIcon = QtGui.QIcon(":/images/dark/theme.svg" if isDarkMode else ":/images/light/theme.svg")
        self.btnDarkMode = QtWidgets.QPushButton(parent=self.footerBar, icon=btnDarkModeIcon, text="")
        self.btnDarkMode.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnDarkMode.setIconSize(QtCore.QSize(24, 24))
        self.btnDarkMode.setFixedSize(30, 30)

        self.btnDarkMode.clicked.connect(self.updateDarkMode)

        btnSettingsIcon = QtGui.QIcon(":/images/dark/settings.svg" if isDarkMode else ":/images/light/settings.svg")
        self.btnSettings = QtWidgets.QPushButton(parent=self.footerBar, icon=btnSettingsIcon, text="")
        self.btnSettings.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnSettings.setIconSize(QtCore.QSize(24, 24))
        self.btnSettings.setFixedSize(30, 30)

        self.footerBarLayout.addWidget(self.btnDarkMode)
        self.footerBarLayout.addWidget(self.btnSettings)

        # Spacer
        self.spacer1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.spacer2 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.spacer3 = QtWidgets.QSpacerItem(10, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        # Adding widgets and items to layout
        self.Layout.addWidget(self.SimulationTitle)
        self.Layout.addWidget(self.frameOpenSimulation)
        self.Layout.addWidget(self.frameDevice)
        self.Layout.addWidget(self.SimulationControls)
        self.Layout.addItem(self.spacer1)
        self.Layout.addWidget(self.logoBottom)
        self.Layout.setAlignment(self.logoBottom, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.Layout.addItem(self.spacer2)
        self.Layout.addWidget(self.footerBar)

    @Slot(QtGui.QMouseEvent)
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):
        print(event.button())
        # return super().mousePressEvent(event)
    
    @Slot(bool)
    def updateDevices(self, ignoreDialogs:bool = False):
        self.closeSerial.emit()

        devices = listPorts()
        TempSettings.set("devices", devices)
        
        self.selectDevice.clear()
    
        if devices:
            self.selectDevice.setDisabled(False)
            self.selectDevice.setPlaceholderText("Selecionar dispositivo")
            for device in devices:
                self.selectDevice.addItem(f"{device[0]} - {device[1]}")

        elif not ignoreDialogs:
            self.selectDevice.setDisabled(True)

            messageBox = QtWidgets.QMessageBox()
            messageBox.setWindowTitle("Nenhum dispositivo encontrado")
            messageBox.setIcon(QtWidgets.QMessageBox.Warning)
            messageBox.setText("Nenhum dispositivo foi encontrado.")
            messageBox.setInformativeText("Conecte um dispositivo e tente novamente.")
            messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)

            messageBox.exec()
        else:
            self.selectDevice.setDisabled(True)
            self.selectDevice.setPlaceholderText("Nenhum disp. encontrado")

    @Slot()
    def updateDarkMode(self):
        isDarkMode = not self.settings.value("darkMode", defaultValue=TempSettings.get("isDarkModeSystem"), type=bool)

        self.toggleDarkMode.emit(isDarkMode)

        self.settings.setValue("darkMode", isDarkMode)

        theme = ""

        if(isDarkMode):
            theme = "dark"
        else:
            theme = "light"

        self.btnUpdateDevices.setIcon(QtGui.QIcon(f":/images/{theme}/update.svg"))
        self.btnDarkMode.setIcon(QtGui.QIcon(f":/images/{theme}/theme.svg"))
        self.btnSettings.setIcon(QtGui.QIcon(f":/images/{theme}/settings.svg"))
        self.logoBottom.load(f":/images/icons/icon_{theme}.svg")
