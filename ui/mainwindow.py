from PySide6 import QtWidgets
from PySide6.QtCore import Qt, Slot, QSettings
from PySide6.QtGui import QIcon
from style.style import globalStyle

from ui.widgets.leftmenu import LeftMenu
from ui.widgets.simulation import AreaSimulation

import resources.resources

# Creating the central widget
class CentralWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QMainWindow):
        super().__init__()
    
        self.setObjectName("CentralWidget")
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.Layout = QtWidgets.QHBoxLayout(self)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.setSpacing(0)

        self.setLayout(self.Layout)

        self.LeftMenu = LeftMenu(self)
        self.AreaSimulation = AreaSimulation(self)

        self.Layout.addWidget(self.LeftMenu)
        self.Layout.addWidget(self.AreaSimulation)

# Creating the main window
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, isDarkMode):
        super().__init__()
        self.settings = QSettings("BrunoCardoso", "SimuladorCircuitosDigitais")

        self.isDarkMode = True if (self.settings.value("darkMode",defaultValue=isDarkMode, type=bool)) else False

        # Defining window parameters
        self.setWindowTitle("Simulador Circuitos Digitais")
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        self.setWindowIcon(QIcon(":/images/icons/icon.ico"))

        self.setStyleSheet(globalStyle(self.isDarkMode))

        self.central = CentralWidget(self)

        self.setCentralWidget(self.central)

    @Slot()
    def closeEvent(self, event):
        QtWidgets.QApplication.quit()
        super().closeEvent(event)