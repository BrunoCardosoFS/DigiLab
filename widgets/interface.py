from PySide6 import QtWidgets, QtCore
from config import Config

class LeftMenu(QtWidgets.QGroupBox):
    def __init__(self, mainWindow):
        super().__init__()

        # Parametros do widget
        self.setFixedWidth(200)

        #Criando o layout principal do widget
        self.layout = QtWidgets.QVBoxLayout(self)

        #Definindo as configurações
        self.settings = QtCore.QSettings("BrunoCardoso", "SimuladorCircuitosDigitais")

        # Parametros do layout
        self.layout.setContentsMargins(10,10,10,10)

        #Definindo a size policy
        policy = self.sizePolicy()
        policy.setVerticalPolicy(QtWidgets.QSizePolicy.Expanding)
        self.setSizePolicy(policy)

        # Criando os widgets filhos
        self.txtSimulation = QtWidgets.QLabel("Simulação", alignment=QtCore.Qt.AlignCenter)
        self.combo_box = QtWidgets.QComboBox()
        self.combo_box.addItem("Tanque")
        self.combo_box.addItem("Semáforo")
        self.combo_box.addItem("Esteira")

        self.controlSimulation = QtWidgets.QGroupBox()
        self.controlSimulation.setObjectName("ControlSimulator")
        self.layoutControlSimulation = QtWidgets.QHBoxLayout(self.controlSimulation)
        self.layoutControlSimulation.setContentsMargins(35,0,35,0)
        self.layoutControlSimulation.setSpacing(5)

        self.buttonPlay = QtWidgets.QPushButton("Play")
        self.buttonStop = QtWidgets.QPushButton("Stop")

        self.buttonPlay.setFixedWidth(40)
        self.buttonPlay.setFixedHeight(30)

        self.buttonStop.setFixedWidth(40)
        self.buttonStop.setFixedHeight(30)


        self.layoutControlSimulation.addWidget(self.buttonPlay)
        self.layoutControlSimulation.addWidget(self.buttonStop)

        self.txtConfigs = QtWidgets.QLabel("Configurações", alignment=QtCore.Qt.AlignCenter)
        self.buttonDarkMode = QtWidgets.QPushButton("Modo claro" if (self.settings.value("darkMode", type=bool)) else "Modo escuro")
        self.buttonOpenConfig = QtWidgets.QPushButton("Configurações")
        self.spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.copyright = QtWidgets.QLabel("Criado por Bruno Cardoso", alignment=QtCore.Qt.AlignCenter)

        # Adicionando elementos ao layout principal
        self.layout.addWidget(self.txtSimulation)
        self.layout.addWidget(self.combo_box)
        self.layout.addWidget(self.controlSimulation)

        self.layout.addWidget(self.txtConfigs)
        self.layout.addWidget(self.buttonDarkMode)
        self.layout.addWidget(self.buttonOpenConfig)

        self.layout.addItem(self.spacer)
        # self.layout.addWidget(self.copyright)

        self.setLayout(self.layout)

        # Chamadas das funções
        self.combo_box.currentIndexChanged.connect(self.election_changed)
        self.buttonDarkMode.clicked.connect(lambda: self.setDarkMode(mainWindow))
        self.buttonOpenConfig.clicked.connect(self.openConfig)

    @QtCore.Slot()
    def election_changed(self, index):
        selected_item = self.combo_box.currentText()
        print(f"Item selecionado: {selected_item}")

    # Abrir janela de configurações
    def openConfig(self):
        self.config = Config()
        self.config.show()

    # DarkMode
    def setDarkMode(self, mainWindow):
        self.varDarkMode = not (self.settings.value("darkMode", type=bool))

        self.settings.setValue("darkMode", self.varDarkMode)
        self.buttonDarkMode.setText("Modo claro" if self.varDarkMode else "Modo escuro")

        mainWindow.setDarkMode()