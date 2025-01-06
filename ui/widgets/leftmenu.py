from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt, Slot

from modules.tempsettings import TempSettings

import resources.resources

class LeftMenu(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setFixedWidth(220)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)

        self.setObjectName("LeftMenu")

        # Layout
        self.Layout = QtWidgets.QVBoxLayout(self)
        self.Layout.setContentsMargins(15, 10, 15, 10)
        self.setLayout(self.Layout)

        #QSettings
        self.settings = QtCore.QSettings("BrunoCardoso", "SimuladorCircuitosDigitais")
        isDarkMode = self.settings.value("darkMode", defaultValue=TempSettings.get("isDarkModeSystem"), type=bool)

        # Title
        self.SimulationTitle = QtWidgets.QLabel(text="Simulação", parent=self, alignment=QtCore.Qt.AlignCenter)

        # Experiment selection
        self.selectSimulation = QtWidgets.QComboBox(self)
        self.selectSimulation.setCursor(QtCore.Qt.PointingHandCursor)
        self.selectSimulation.setPlaceholderText("Selecionar experimento")
        
        self.selectSimulation.addItem("Tanque")
        self.selectSimulation.addItem("Semáforo")
        self.selectSimulation.addItem("Esteira")

        # Device selection
        self.selectDevice = QtWidgets.QComboBox(self)
        self.selectDevice.setCursor(QtCore.Qt.PointingHandCursor)
        self.selectDevice.setPlaceholderText("Selecionar dispositivo")

        # Simulation controls
        self.SimulationControls = QtWidgets.QWidget(self)
        self.SimulationControls.setObjectName("SimulationControls")
        self.SimulationControlsLayout = QtWidgets.QHBoxLayout(self.SimulationControls)
        self.SimulationControlsLayout.setContentsMargins(0, 0, 0, 0)
        self.SimulationControlsLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.btnPlay = QtWidgets.QPushButton(parent=self.SimulationControls, icon=QtGui.QIcon(":/images/icons/play.svg"), text="")
        self.btnPlay.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnPlay.setFixedSize(30, 30)

        self.btnStop = QtWidgets.QPushButton(parent=self.SimulationControls, icon=QtGui.QIcon(":/images/icons/stop.svg"), text="")
        self.btnStop.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnStop.setFixedSize(30, 30)

        self.SimulationControlsLayout.addWidget(self.btnPlay)
        self.SimulationControlsLayout.addWidget(self.btnStop)

        # Spacer
        self.spacer1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.spacer2 = QtWidgets.QSpacerItem(10, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        # Logo
        logoBottomPixmap = QtGui.QPixmap(":/images/icons/icon_dark.svg" if isDarkMode else ":/images/icons/icon_light.svg").scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logoBottom = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter, text="")
        self.logoBottom.setPixmap(logoBottomPixmap)

        # Footer Bar
        self.footerBar = QtWidgets.QWidget(self)
        self.footerBar.setObjectName("FooterBar")
        self.footerBar.setAttribute(Qt.WA_StyledBackground, True)
        self.footerBar.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        self.footerBarLayout = QtWidgets.QHBoxLayout(self.footerBar)
        self.footerBarLayout.setContentsMargins(10, 10, 10, 0)

        btnDarkModeIcon = QtGui.QIcon(":/images/dark/sun.svg" if isDarkMode else ":/images/light/moon.svg")
        self.btnDarkMode = QtWidgets.QPushButton(parent=self.footerBar, icon=btnDarkModeIcon, text="")
        self.btnDarkMode.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnDarkMode.setIconSize(QtCore.QSize(24, 24))
        self.btnDarkMode.setFixedSize(30, 30)

        btnSettingsIcon = QtGui.QIcon(":/images/dark/settings.svg" if isDarkMode else ":/images/light/settings.svg")
        self.btnSettings = QtWidgets.QPushButton(parent=self.footerBar, icon=btnSettingsIcon, text="")
        self.btnSettings.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnSettings.setIconSize(QtCore.QSize(24, 24))
        self.btnSettings.setFixedSize(30, 30)

        self.footerBarLayout.addWidget(self.btnDarkMode)
        self.footerBarLayout.addWidget(self.btnSettings)



        # Adding widgets and items to layout
        self.Layout.addWidget(self.SimulationTitle)
        self.Layout.addWidget(self.selectSimulation)
        self.Layout.addWidget(self.selectDevice)
        self.Layout.addWidget(self.SimulationControls)
        self.Layout.addItem(self.spacer1)
        self.Layout.addWidget(self.logoBottom)
        self.Layout.addWidget(self.footerBar)
        