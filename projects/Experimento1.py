from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Slot, Qt

class Componente(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)


class Projeto(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.values = ["0","0","0","0","0","0","0","0","0","0"]

        self.Layout = QtWidgets.QVBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)

        self.menu = QtWidgets.QWidget(parent=self)
        self.menuLayout = QtWidgets.QVBoxLayout(self.menu)

        self.Layout.addWidget(self.menu)

        self.btnLoad1 = QtWidgets.QPushButton(parent=self.menu, text="Componente 1")
        self.btnLoad1.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

        self.btnLoad2 = QtWidgets.QPushButton(parent=self.menu, text="Componente 2")
        self.btnLoad2.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

        self.btnLoad3 = QtWidgets.QPushButton(parent=self.menu, text="Componente 3")
        self.btnLoad3.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

        self.btnLoad4 = QtWidgets.QPushButton(parent=self.menu, text="Componente 4")
        self.btnLoad4.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

        self.menuLayout.addWidget(self.btnLoad1)
        self.menuLayout.addWidget(self.btnLoad2)
        self.menuLayout.addWidget(self.btnLoad3)
        self.menuLayout.addWidget(self.btnLoad4)

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