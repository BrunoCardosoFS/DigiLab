from PySide6 import QtWidgets, QtCore, QtGui
import resources.resources

class TruthTable(QtWidgets.QGroupBox):
    def __init__(self, parent: None):
        super().__init__()
        self.isDarkMode = parent.isDarkMode
        self.parent = parent

        # Parametros do widget
        self.setFixedWidth(220)

        #Definindo a size policy
        policy = self.sizePolicy()
        policy.setVerticalPolicy(QtWidgets.QSizePolicy.Expanding)
        self.setSizePolicy(policy)

        #Criando o layout principal do widget
        self.layout = QtWidgets.QVBoxLayout(self)

        #Definindo QSettings
        self.settings = QtCore.QSettings("BrunoCardoso", "SimuladorCircuitosDigitais")
        getDarkMode = self.settings.value("darkMode", defaultValue=self.isDarkMode, type=bool)

        # Parametros do layout
        self.layout.setContentsMargins(15,10,15,25)
        