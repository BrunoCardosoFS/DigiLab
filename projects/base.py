from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Slot, Signal
from PySide6.QtCore import Qt


class Projeto(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        self.values = ["0","0","0","0","0","0","0","0","0","0"]

        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        self.Layout = QtWidgets.QVBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)

    @Slot()
    def resetSimulation(self):
        pass

    @Slot(list)
    def updateSimulation(self, data: list):
        pass

    @Slot()
    def getValues(self):
        self.values[0] = str(1)

        return self.values