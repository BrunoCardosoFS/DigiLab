from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt, Slot

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

        # Spacers
        self.spacer1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.spacer2 = QtWidgets.QSpacerItem(10, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

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


        # Adding widgets and items to layout
        self.Layout.addWidget(self.SimulationTitle)
        self.Layout.addWidget(self.selectSimulation)
        self.Layout.addWidget(self.selectDevice)
        self.Layout.addWidget(self.SimulationControls)
        self.Layout.addItem(self.spacer1)
        