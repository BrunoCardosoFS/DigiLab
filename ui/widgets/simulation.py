from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6.QtCore import Qt

import os

class Simulation(QtWidgets.QWidget):
    # testeSignal = QtCore.Signal(dict)

    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)

        self.setMinimumWidth(50)
        self.setMinimumHeight(50)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #f00;")
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)

        self.Layout = QtWidgets.QVBoxLayout(self)
    
    @QtCore.Slot()

    def testeSlot(self, lista: dict):
        print(lista)


class AreaSimulation(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        
        self.setObjectName("AreaSimulation")
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.Layout = QtWidgets.QVBoxLayout(self)
        self.Layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(self.Layout)

        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # Scroll Area
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("SimulationScrollArea")

        self.scrollAreaWidget = QtWidgets.QWidget(self.scrollArea)
        self.scrollAreaWidget.setObjectName("SimulationScrollAreaWidget")
        self.layoutScrollAreaWidget = QtWidgets.QVBoxLayout(self.scrollAreaWidget)
        self.layoutScrollAreaWidget.setContentsMargins(3,3,3,3)

        self.scrollArea.setWidget(self.scrollAreaWidget)

        self.spacerTop = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.spacerBottom = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.layoutScrollAreaWidget.addItem(self.spacerTop)

        self.simulation = Simulation(self.scrollAreaWidget)
        self.layoutScrollAreaWidget.addWidget(self.simulation)

        self.layoutScrollAreaWidget.addItem(self.spacerBottom)

        self.Layout.addWidget(self.scrollArea)
        