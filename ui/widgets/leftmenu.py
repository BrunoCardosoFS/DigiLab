from PySide6 import QtWidgets
from PySide6.QtCore import Qt, Slot

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setObjectName("LeftMenu")
        self.setAttribute(Qt.WA_StyledBackground, True)