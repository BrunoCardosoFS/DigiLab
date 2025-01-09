from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Slot
from PySide6.QtCore import Qt

import os

class Projeto(QtWidgets.QWidget):

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)

        self.setAttribute(Qt.WA_StyledBackground, True)

        self.setStyleSheet("Projeto{background-color: blue; border: 3px solid #000;}")
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        self.Layout = QtWidgets.QHBoxLayout(self)

        self.setFixedSize(700, 700)

        button = QtWidgets.QPushButton("Send Data", self)
        button.setFixedWidth(100)

        button.move(15, 30)