from PySide6 import QtWidgets
from PySide6.QtCore import Qt, Slot

class AreaSimulation(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        
        self.setObjectName("AreaSimulation")
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.Layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.Layout)

        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        