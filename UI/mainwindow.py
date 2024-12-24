from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QIcon

from PySide6 import QtWidgets

import resources.resources

# Creating the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Defining window parameters
        self.setWindowTitle("Simulador Circuitos Digitais")
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        self.setWindowIcon(QIcon(":/images/icons/icon.ico"))

        self.setStyleSheet("#CentralWidget{background-color: #181818;}")

        self.central = QWidget(self)
        self.central.setObjectName("CentralWidget")
        self.central.setAttribute(Qt.WA_StyledBackground, True)

        self.layoutCentral = QHBoxLayout(self.central)
        self.layoutCentral.setContentsMargins(0, 0, 0, 0)
        self.layoutCentral.setSpacing(0)

        self.central.setLayout(self.layoutCentral)

        self.setCentralWidget(self.central)

    @Slot()
    def closeEvent(self, event):
        QtWidgets.QApplication.quit()
        super().closeEvent(event)