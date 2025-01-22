from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt

from ui.widgets.simulationHome import Projeto

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
        self.layoutScrollAreaWidget.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.scrollArea.setWidget(self.scrollAreaWidget)
        
        self.Layout.addWidget(self.scrollArea)

        # Add tanque
        self.projeto = Projeto()
        self.layoutScrollAreaWidget.addWidget(self.projeto)

    @Slot(list)
    def receiveData(self, data: list):
        if not self.projeto.useHardware:
            self.projeto.updateSimulation([])
        elif len(data) == 10:
            self.projeto.updateSimulation(data)
        