from PySide6 import QtWidgets, QtCore, QtGui
from config import Config
import resources.resources

class LeftMenu(QtWidgets.QGroupBox):
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

        #Definindo as configurações
        self.settings = QtCore.QSettings("BrunoCardoso", "SimuladorCircuitosDigitais")
        getDarkMode = self.settings.value("darkMode", defaultValue=self.isDarkMode, type=bool)

        # Parametros do layout
        self.layout.setContentsMargins(15,10,15,25)

        # Definindo o logoBottomImage
        logoBottomImage = QtGui.QPixmap(":/images/icons/icon_dark.svg" if getDarkMode else ":/images/icons/icon_light.svg").scaled(90, 90)

        # Criando os widgets filhos
        self.txtSimulation = QtWidgets.QLabel("Simulação", alignment=QtCore.Qt.AlignCenter)

        self.logoBottom = QtWidgets.QLabel("Teste", alignment=QtCore.Qt.AlignCenter)
        self.logoBottom.setPixmap(logoBottomImage)

        self.selectSimulation = QtWidgets.QComboBox()
        self.selectSimulation.setPlaceholderText("Selecionar experimento")
        self.selectSimulation.addItem("Tanque")
        self.selectSimulation.addItem("Semáforo")
        self.selectSimulation.addItem("Esteira")

        self.selectDevice = QtWidgets.QComboBox()
        self.selectDevice.setPlaceholderText("Selecionar dispositivo")
        self.selectDevice.addItem("COM1 - USB Serial")
        self.selectDevice.addItem("COM2 - Bluetooth Serial")
        self.selectDevice.addItem("COM3")

        self.inputExpression = QtWidgets.QLineEdit()
        self.inputExpression.setPlaceholderText("Digite a expressão lógica")

        # Criando os controles da simulação
        self.controlSimulation = QtWidgets.QGroupBox()
        self.controlSimulation.setObjectName("ControlSimulator")
        self.layoutControlSimulation = QtWidgets.QHBoxLayout(self.controlSimulation)
        self.layoutControlSimulation.setContentsMargins(30,0,30,0)
        self.layoutControlSimulation.setSpacing(5)

        self.buttonOpen = QtWidgets.QPushButton()
        self.buttonPlay = QtWidgets.QPushButton()
        self.buttonStop = QtWidgets.QPushButton()

        self.buttonOpen.setIcon(QtGui.QIcon(":/images/icons/open.svg"))
        self.buttonPlay.setIcon(QtGui.QIcon(":/images/icons/play.svg"))
        self.buttonStop.setIcon(QtGui.QIcon(":/images/icons/stop.svg"))

        self.buttonOpen.setFixedWidth(30)
        self.buttonOpen.setFixedHeight(30)

        self.buttonPlay.setFixedWidth(30)
        self.buttonPlay.setFixedHeight(30)

        self.buttonStop.setFixedWidth(30)
        self.buttonStop.setFixedHeight(30)

        self.layoutControlSimulation.addWidget(self.buttonOpen)
        self.layoutControlSimulation.addWidget(self.buttonPlay)
        self.layoutControlSimulation.addWidget(self.buttonStop)

        self.txtConfigs = QtWidgets.QLabel("Configurações", alignment=QtCore.Qt.AlignCenter)
        self.buttonDarkMode = QtWidgets.QPushButton("Modo claro" if getDarkMode else "Modo escuro")
        self.buttonOpenConfig = QtWidgets.QPushButton("Configurações")
        self.spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.bottomSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.copyright = QtWidgets.QLabel("Criado por Bruno Cardoso", alignment=QtCore.Qt.AlignCenter)

        # Adicionando elementos ao layout principal
        self.layout.addWidget(self.txtSimulation)
        self.layout.addWidget(self.selectSimulation)
        self.layout.addWidget(self.selectDevice)
        self.layout.addWidget(self.inputExpression)
        self.layout.addWidget(self.controlSimulation)

        self.layout.addItem(self.spacer)
        self.layout.addWidget(self.txtConfigs)
        self.layout.addWidget(self.buttonDarkMode)
        self.layout.addWidget(self.buttonOpenConfig)

        self.layout.addItem(self.bottomSpacer)
        self.layout.addWidget(self.logoBottom)
        # self.layout.addWidget(self.copyright)

        self.setLayout(self.layout)

        # Chamadas das funções
        self.selectSimulation.currentIndexChanged.connect(self.election_changed)
        self.buttonDarkMode.clicked.connect(lambda: self.setDarkMode(parent))
        self.buttonOpenConfig.clicked.connect(self.openConfig)

    @QtCore.Slot()
    def election_changed(self, index):
        selected_item = self.selectSimulation.currentText()
        print(f"Item selecionado: {selected_item}")

    # Abrir janela de configurações
    def openConfig(self):
        self.config = Config(self)
        self.config.show()

    # DarkMode
    def setDarkMode(self, mainWindow):
        self.varDarkMode = not (self.settings.value("darkMode", type=bool))

        self.settings.setValue("darkMode", self.varDarkMode)
        self.buttonDarkMode.setText("Modo claro" if self.varDarkMode else "Modo escuro")
        logoBottomImage = QtGui.QPixmap(":/images/icons/icon_dark.svg" if self.varDarkMode else ":/images/icons/icon_light.svg").scaled(90, 90)
        self.logoBottom.setPixmap(logoBottomImage)

        mainWindow.setDarkMode()