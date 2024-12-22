from PySide6 import QtWidgets
from PySide6.QtGui import QIcon

import resources.resources

# Criando a janela principal
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Definindo os parametros da janela
        self.setWindowTitle("Simulador Circuitos Digitais")
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        self.setWindowIcon(QIcon(":/images/icons/icon.ico"))