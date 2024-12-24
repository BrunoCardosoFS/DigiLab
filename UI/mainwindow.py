from PySide6 import QtWidgets
from PySide6.QtCore import Qt, Slot, QSettings
from PySide6.QtGui import QIcon
from style.style import globalStyle

import resources.resources

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

        self.central = QtWidgets.QWidget(self)
        self.central.setObjectName("CentralWidget")
        self.central.setAttribute(Qt.WA_StyledBackground, True)

        self.layoutCentral = QtWidgets.QHBoxLayout(self.central)
        self.layoutCentral.setContentsMargins(0, 0, 0, 0)
        self.layoutCentral.setSpacing(0)

        self.central.setLayout(self.layoutCentral)

        self.setCentralWidget(self.central)

    @Slot()
    def closeEvent(self, event):
        QtWidgets.QApplication.quit()
        super().closeEvent(event)