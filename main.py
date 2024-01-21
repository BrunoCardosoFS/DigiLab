import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QIcon

current_path = sys.argv[0].replace("main.py", "")

from widgets.leftMenu import LeftMenu
from widgets.simulation import Simulation, SimulationScene
from styles.style import globalStyle
import resources.resources

# Criando a area da simulação
class AreaSimulation(QtWidgets.QGraphicsView):
    def __init__(self, parent: None):
        super().__init__()
        self.setRenderHint(QtGui.QPainter.Antialiasing, True)
        self.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)

        self.policy = self.sizePolicy()
        self.policy.setVerticalPolicy(QtWidgets.QSizePolicy.Expanding)
        self.policy.setHorizontalPolicy(QtWidgets.QSizePolicy.Expanding)
        self.setSizePolicy(self.policy)

        self.simulation = SimulationScene(self)
        self.simulation.setObjectName("Simulation")

        self.setScene(self.simulation)

        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)  # Ativar a capacidade de arrastar a visualização

    def wheelEvent(self, event):
        if event.modifiers() & QtCore.Qt.ControlModifier:
            # Aumentar ou diminuir o zoom com base na roda do mouse
            factor = 1.2  # Fator de escala para zoom

            if (event.angleDelta().y() < 0):
                factor = 1.0 / factor  # Zoom out
            
            self.scale(factor, factor)
        else:
            # Chamar a implementação padrão para outros casos
            super().wheelEvent(event)


# Criando a janela principal
class WindowSimulator(QtWidgets.QMainWindow):
    def __init__(self, isDarkMode: type=bool):
        super().__init__()
        self.isDarkMode = isDarkMode
        
        # Definindo os parametros da janela
        self.setWindowTitle("Simulador Circuitos Digitais")
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        self.setWindowIcon(QIcon(":/images/icons/icon.ico"))

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

        self.areaSimulation = AreaSimulation(self)
        self.areaSimulation.setObjectName("AreaSimulation")

        # Adicionando os widgets o layout principal
        self.layout.addWidget(self.leftMenu)
        self.layout.addWidget(self.areaSimulation)

        # Definindo os estilos
        self.container.setStyleSheet(globalStyle(self)) 

        # Adicionando container como widget principal
        self.setCentralWidget(self.container)

        # Chamadas das funções

    @QtCore.Slot()
    # Verificar se a janela principal foi fechada e encerrar o programa
    def closeEvent(self, event):
        sys.exit(app.exec())

    def setDarkMode(self):
        self.container.setStyleSheet(globalStyle(self))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle("Fusion")

    # Obtém a cor da janela
    corJanela = app.palette().color(QtGui.QPalette.Window)

    # Verifica o modo de aparência com base na luminosidade da cor da janela
    isDarkMode = False if corJanela.lightnessF() > 0.5 else True

    # Instanciando a janela principal
    widget = WindowSimulator(isDarkMode)
    # Definindo o tamanho inicial da janela
    widget.resize(800, 500)
    # Mostrando a janela principal
    widget.show()

    sys.exit(app.exec())