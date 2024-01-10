import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QIcon

current_path = sys.argv[0].replace("main.py", "")

from config import Config
from widgets.leftMenu import LeftMenu
from styles.style import globalStyle
import resources.resources

class WindowSimulator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Definindo os parametros da janela
        self.setWindowTitle("Simulador Circuitos Digitais")
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        self.setWindowIcon(QIcon(":/images/icons/icon.ico"))

        # Definindo as configurações
        self.settings = QtCore.QSettings("BrunoCardoso", "SimuladorCircuitosDigitais")
        self.settings.setValue("darkMode", self.settings.value("darkMode", defaultValue=True, type=bool))

        # Criando o Widget principal da janela
        self.container = QtWidgets.QWidget()
        self.container.setObjectName("centralwidget")

        # Criando o layout do widget principal
        self.layout = QtWidgets.QHBoxLayout(self.container)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)

        # Criando os widgets filhos
        self.leftMenu = LeftMenu(self)
        self.leftMenu.setObjectName("LeftMenu")

        self.areaSimulator = QtWidgets.QGroupBox()
        self.areaSimulator.setObjectName("AreaSimulator")
        self.layoutAreaSimulator = QtWidgets.QVBoxLayout(self.areaSimulator)


        # Adicionando os widgets o layout principal
        self.layout.addWidget(self.leftMenu)
        self.layout.addWidget(self.areaSimulator)

        # Definindo os estilos
        self.container.setStyleSheet(globalStyle()) 

        # Adicionando container como widget principal
        self.setCentralWidget(self.container)

        # Chamadas das funções

    @QtCore.Slot()
    # Verificar se a janela principal foi fechada e encerrar o programa
    def closeEvent(self, event):
        sys.exit(app.exec())

    def setDarkMode(self):
        self.container.setStyleSheet(globalStyle())

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle("Fusion")

    # Instanciando a janela principal
    widget = WindowSimulator()
    # Definindo o tamanho inicial da janela
    widget.resize(800, 500)
    # Mostrando a janela principal
    widget.show()

    sys.exit(app.exec())