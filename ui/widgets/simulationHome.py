from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Slot, Qt
from PySide6.QtSvgWidgets import QSvgWidget, QGraphicsSvgItem
import math


class Projeto(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.useHardware = False
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        self.Layout = QtWidgets.QVBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)

        self.svg = QSvgWidget(":/images/icons/icon-text.svg", parent=self)
        fwidget = 500
        fheight = int(fwidget * (307/1132))
        self.svg.setFixedSize(fwidget, fheight)

        self.Layout.addWidget(self.svg)

    @Slot()
    def resetSimulation(self):
        pass

    @Slot(list)
    def updateSimulation(self, data: list):
        pass

    @Slot()
    def getValues(self):
        return ["0","0","0","0","0","0","0","0","0","0"]