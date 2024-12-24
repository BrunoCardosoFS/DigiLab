from PySide6 import QtWidgets
from PySide6.QtCore import Qt, Slot

class LeftMenu(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__()
        
        self.setObjectName("LeftMenu")
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.Layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.Layout)

        self.setFixedWidth(220)
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        