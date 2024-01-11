from PySide6 import QtWidgets, QtCore, QtGui
import resources.resources

class Tanque(QtWidgets.QGroupBox):
    def __init__(self, params):
        super().__init__()

        #Criando o layout principal do widget
        self.layout = QtWidgets.QVBoxLayout(self)

        #Definindo as configurações
        self.settings = QtCore.QSettings("BrunoCardoso", "SimuladorCircuitosDigitais")

        # Parametros do layout
        self.layout.setContentsMargins(10,10,10,25)

        self.setStyleSheet("QGroupBox{border: 2px solid #000}")

        #Definindo a size policy
        policy = self.sizePolicy()
        policy.setVerticalPolicy(QtWidgets.QSizePolicy.Minimum)
        policy.setHorizontalPolicy(QtWidgets.QSizePolicy.Minimum)
        self.setSizePolicy(policy)

        print(params)

        # Criando os widgets filhos
        self.txtSimulation = QtWidgets.QLabel("Tanque", alignment=QtCore.Qt.AlignCenter)

        # Adicionando elementos ao layout principal
        self.layout.addWidget(self.txtSimulation)

        self.setLayout(self.layout)

        # Chamadas das funções
        

    @QtCore.Slot()
    def openConfig(self):
        pass